- Proposed by Eric Brewer, and proved by Gilbert and Lynch

- A distributed (storage) system you can satisfy at most 2 out of 3 guarantees
    - Consistency: all nodes see same data at any time or reads return latest written value by the client
    - Availability: the system allows operations all the time and operations return quickly
    - Partition Tolerance: The system continues to work in spite of network partition/failures.
    
-  Availability: (A)
    - Read/writes complete reliably and quickly (directly related to revenue)
    
- Consistency (C)
    - All nodes should see the same data or reply back in the same data (example, banks and flights)
    
- Partition: (P)
    - Happens when datacenters get disconnected, DNS not working, intra datacenter outages
    
- Partition tolerance is really required, else information is offline
    - Cassandra chooses Availability and Partition Tolerance
    - It provides eventual consistency
    - My SQL provides strong consistency
    - AC : Relation DBMS single server
    - AP : Cassandra, Riak, Voldemort
    - CP : BigTable, Spanner, HBase
    
- What is Eventual Consistency?
    - Given a key, support all writes to key stop
    - Then all replicas of key converge to one value preferably the latest one
    - In real life, convergence is always catching up the moving write wave
    - Since there is a lag between convergence and writes, read operation may return stale values
    - Basically Available Soft state Eventual Consistency (BASE in Cassandra vs RDBMS ACID)
    
- In cassandra, you need X replicas to send an acknowledgement
    - How is X selected?
        - Cassandra has consistency levels
        - Client chooses a consistency level for an operation (read/write)
        - Consistency level refers to how many replicas the client needs to talk to before sending back the result
          of read/write operation
        - Consistency Levels can be
            - ANY: any server (may not be replica) { coordinator can cache write and reply quickly to client)
            - ALL : all servers are updated, the slowest operation
            - ONE : at least one replica, faster than ALL but cannot tolerate a failure
            - QUORUM : quorum across all replicas in all datacenters
                - quorum represent majority set of nodes
                - if a write happens to a quorum and read happens from a different quorum, then it gives stronger
                consistency at a better speed than ALL
                  
                - Let 1, 2, 3, 4, 5 be 5 servers arranged in a ring
                - Quorum1 :  consists of 1, 2, 3 (abbv as Q1)
                - Quorum2 : consists of 3, 4, 5 (abbv as Q2)
                - Both are having majority elements (3 out 5) respectively
                - If write happens to Q1 and read from Q2, due to common node 3, we get a better consistency
    
    - Quorum Reads
        - Client specifies value of R (<= N (total number of replicas of that key))
        - R = read consistency level
        - Coordinator waits for R replicas to respond before sending result to client
        - In background, coordinator check N - R replicas and initiates a read repair if needed
    - Quorum Writes
        - Client specifies a W (Write consistency level)
        - Client writes new values to W replicas and returns
            - Coordinator blocks until quorum is reached
            - Ascynchronous: Just write and return 
    
    - Two necessary conditions
        1. W + R > N : ensures that if you have a write quorum and a read quorum, they intersect at atleast one server, reads will return the latest write
        2. W + W > N : ensures that if you have two write quorums, they intersect at one server and latest write is persisted
        
    - W = 1, R = 1: very few writes and reads
    - W = N, R = 1: great for read heavy workloads
    - W = (N/2) + 1, R = (N/2) + 1 : greater for write heavy workloads
    - W = 1, R = N : great for write heavy workloads with mostly one client writing per key (ensures strong reading)
    
    - Other consistency levels
        - Consider 3 data centers with 3 replicas in each ( total 9 replicase)
        - QUORUM : quorum across all replicas in all datacenters ( needs 5 replicas to make a choice)
        - LOCAL QUORUM : quorum in coordinator's data center (needs 2 replicas to make a choice)
        - EACH QUORUM : quorum in each DC (2 replicase in all 3 quorums needed to make a choice)
        
        
    
    
            