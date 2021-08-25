 - Intro
    - Distributed key value store, can run on single or multiple data centers
    -  Originally designed in FB, now open source
    - Netflix uses cassandra to keep track of your current position in the video that you're watching
     
- Given a key value pair, how do you map the key to a server?
    - Cassandra uses P2P consistent hashing ring
    - Key gets stored at a server which is a successor to the query hash in the map
    - There may be primary or backup replica
    - Cassandra does not have fingers table, each server that runs cassandra has a separate consistent hashing ring.
    - Mapping from key to server is called partitioner
    
    - Replication Strategies:
        - Simple Strategy
            - Random Partitioner: Chord like hash partitioning
            - Byte Order Partitioner: Assign ranges of keys to servers, useful for range queries
        - Network Topology Strategy:
            - for multi data center deployments
            - replica storage algorithm:
                - First replica placed according to partitioner
                - Travel clockwise in ring until you get a different rack
    
    - Cassandra in detail
      - Cassandra uses snitches for mapping IPs to racks and Datacenters (configurable by cassandra.yml)
          - SimpleSnitch: Unaware of topology
          - RackInfering: Assumes topology of network by octet of server's IP address
            - It assumes an ip address which is a collection of 4 octets such as 
                <oct1>.<oct2>.<oct3>.<oct4> = <ignored>.<DC octet>.<rack octet>.<node octet>
                ie if an IP is 101.102.103.104, DC octet = 102, rack octet = 103, node octet = 104
                This is an assumption based config, not accurate or actual
                
          - Property file snitch: If the user knows the ip address of data center and racks, the user can configure it in a property file
          - EC2 Snitch: uses EC2, EC2 region = Data center and Availability Zone = rack addresses
    
      -  Writes in Cassandra:
        - Since cassandra works on write heavy workloads, it needs to be fast
        - Cassandra cluster has coordinaters and partitioners:
            - Partitioners: It is incharge of defining which node should store given data
            - Coordinaters: Client read or write requests can be sent to any node in the cluster
            and when a client connects to a node with a request, that node serves as the coordinator for that particular
              client operation
              
            - Coordinator may be per key, per client or per query
            - Per key cooridinator ensures writes for the key are serialized
            - Coordinator uses partitioner to send query to all replica nodes responsible for key
            - When X replicas respond coordinator returns an acknowledgement to the client
            - System needs to be always writable
                - If while writing any replica is down the coordinator writes to all other replicas and keeps the "write" locally until down replica comes back up
                - When all replicas are down then the Coordinator buffers writes for up to a few hours
                - This mechanism is known as hinted handoff
            - One ring per datacenter: (DC)
                - Per DC coordinator is elected to coordinate with other datacenters to make sure data center to data center is done in a correct manner
                - This cooridnator is different from the query handling coordinator
                - Election of coordinator is done by Zookeeper using Paxos
          
        - Writes at replica node (What happens when a replica node receives a write request)
            - Logs the info about write in a disk, used for failure recovery.
            - Makes changes to  write back cache called memtable, which stores the data back in database after sometime 
            - Its a cache that can be searched by key, insert or update
            - Write back cache is faster than a write through cache
            - When memtable is full or memtable is old it is written back to a data file called SSTable, (sorted string table)
            - Index file of SSTable (contains keys in sorted order, position in sstable)
            - Usage of bloom filter to detect membership.
            - Bloom filter checks membership, and has probability of false positives, never false negatives
            - Over time, when multiple sstables are accumulated on the disk, a process of compaction merges different
            sstables by merging updates for a key
            - This is run periodically and locally at each server
        
        - Deletion happens by tombstone, which is a marker to keys that are to be deleted
        - When compaction happens it will delete the item marked with tombstone
            
        - Reads in Cassandra
                - Coordinator contacts X replicas and sends read requests to replicas that have responded quickest in past
                - When X replicas respond, coordinator returns the latest timestamped value from among these X
            
            - Coordinator fetches values from other replicas
                - Check consistency in background, initiates a read repair if any two value are different
                -  This brings all the replicas up to date
            - Reads are slow, but why?
                - A row can be stored as key value pairs in multiple sstables 
                  so fetching each value is slow but slower than write
                  
        - Memebership
            - All servers need to know about every other server in cluster, so every server needs to maintain a list
            of all the other servers that are currently in the server
              
            - List need to be updated automatically as servers join, leave and fail
            - Cassandra uses gossip based cluster membership
        - Suspicion mechanism: 
            - Cassandra adaptively detects failure of a server
            - Suspicion mechanisms set the timeout based on underlying network and failrue detectors
            - Failure detector is called Accrual Detector, it outputs a value representing suspicion
            - This value is calle PHI
            - PHI calculation for a member
                - Inter arrival times for gossip messages
                - PHI(t) = - log(CDF or Probability(t_now - t_last)) / log 10 
                - PHI basically determines the detection timeout, but takes into account historical inter arrival time variations
                for gossip heartbeats. (Slow servers are given higher timeout before they are marked as failures)
                  
        - Cassandra vs MySQL 
            - data load: 50 GB + 
            - MY SQL: {writes : 300 ms, reads: 350 ms}
            - Cassandra : {writes: 0.12 ms, reads: 15 ms}
    
        