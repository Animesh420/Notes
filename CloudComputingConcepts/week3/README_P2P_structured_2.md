- Pastry
    - Similar to Chord, nodes are assigned ids and put in a virtual ring
    - Routing tables use prefix matching (routing is O(LogN))
    - Takes care of underlying network topology
    
    - Example: Let a peer have id 01110100101
        - Then it maintains a neighbor peer with an id matching each of the following prefix
            - \*, 0\*, 01*, 011* and so on... \* means the first bit that differs
        - When the peer needs to forward to an ip lets say
        01110111001, the target differs at 6th bit, so the peer forwards the call
        to the largest prefix matching peer which is 011101\*
          
        - This is a O(logN) process
        - If multiple neighbors have same prefix then that neighbor is chosen which has the smallest internet round trip time
        - Since shorter prefixes have many more candidates (spread through the internet) the neighbors for short prefixes are likely to be closer than the neighbors for longer prefix, thus early hops are short
          and later hops are longer
          
        - Yet overall "stretch" compared to direct Internet path, stays short, pastry uses a stabilization protocol
    
- Kelips (A 1 hop lookup DHT)
    - Uses k affinity groups, k is about sqrt(N)
    - Each peer is hashed and mapped to a group , (hash(peer) mod k)
    - Each peer knows almost all other peers in its own affinity group
    - Each node has 1 contact node in another affinity group
    - Each affinity group has (sqrt(n)) peers
    - Each peer has therefore (sqrt(n) - 1) (peers in same aff. group) + (sqrt(n)) One peer per other aff group
    since there are k=sqrt(N) aff group, total peer per node is approx 2*sqrt(n)
    - The files do not get stored on peers, it is stored only on the peer where it was uploaded
    - A file is hashed by its file name   
    - Let the configuration be
        - Aff group 0 : Peers 129, 30 ...
          Aff group 1 : Peers 15, 160 ...
          Aff group K-1 : Peers 76, 18, 167 ...
      
        For node 160, it knows about all peers in affinity group 1, and 1 peer in each affinity group 0 to K-1.
        This is how it has 2 * sqrt(N) peers.
    
    - All nodes in the group replicate pointer information i.e. metadata about the file, and ip address and port number
      
    - Inserting a file: A node (origin node) that wants to insert a given file f, maps the file name  
      by taking (hash(file) mode k) to the appropriate affinity group, 
      and sends an insert request to the topologically to the closest known contact for that affinity group. 
      This contact picks a node h from its affinity group, 
      uniformly at random, and forwards the insert request to it. The node h is now the homenode of the file.
      The file is transferred from the origin to the homenode.
    -  Lookup :
        - Hash the file name and find the target affinity group 
        - Attempt to connect to the target affinity group from your own
        - If you fail, find another contact from the same affinity group as yours and try to connect it to the contact in target affinity group
        - It is leveraging replicated meta information, lookup cost is O(1), memory cost is O(sqrt(N))
    
    - Membership updates:
        - Based on gossip protocol, inter affinity group and intra affinity group
        - Querying node has flexibility to choose from multiple options
    
    - File metadata:
        - Needs to refreshed periodically from source node
        - If you have a file in system, the owner node has to send heartbeats
        ****

        