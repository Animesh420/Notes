- Structured P2P Systems are precursor to No-SQL or key-value based storage

- Distributed Hash table (DHT)
    - A hash table allows you to insert, lookup and delete objects with keys 
    - A distributed hash table allows you to do the same in a distributed setting (objects=files)
    - Performance concerns
        - Load Balancing - Equal load on all peers
        - Fault tolerance - Replication to maintain availability
        - Efficiency of lookup and insert
        - Locality - The messages should be transferred to the nearest nodes in the network topology
    - Napster, GNutella, Fastrack are all DHTs
- Chord 
  
    -  Time Complexity of Hash Table Operation on all P2P systems
        - Napster
            - Memory: O(1) at the client and O(N) at the server (because server stores all the necessary client information)
            - Lookup Latency: O(1) : One round trip time from a client to napster server ignoring server lookup time in its ternary tree
            - No of messages for a lookup: O(1): One round trip message for finding  the right peer
    
        - GNutella
            - Memory: O(N) as all the peers maintain information about a certain portion of the network
            - Lookup Latency: O(N) as peers need to talk to many of peers in order to get information
            - No of messages for a lookup: O(N) as peers are talking to many peers
    
        - Chord:
            Memory, Lookup Latency, No of messages are O(Log(N))
          
    - Was developed by researchers from Berkley and MIT
    - Each of nodes in P2P overlay selects its neighbor in an intelligent fashion
    - In GNutella neighbors are selected based on number of files/kilobytes shared using ping and pong
    
    - Consistent Hashing - (Hashing on a circle)
        
        - Take ip address and port number of a peer and apply SHA on it, you get 160 bit string
        - You truncate it to m bit  string (m is a system parameter)
        - This gives you a peer id which is a number between 0 to 2^m - 1
        - This means we can map 2^m logical points on a circle.
        - Preferred to have 2^m >> N, where N is the total expected number of peers in the system
        
        - Each peer is identified by its peer id and assigned to a point on a circle
        - For m = 7, we are looking at 0 to 127 peers
          
        - PEER POINTERS
            - Each pair knows about its successor (node in clockwise) and predecessors (node in anti-clockwise)
            - Finger table peer pointer : useful to route your queries fairly quickly
                - Let m = 7, finger table runs from 0 to m-1 i.e. 0 to 6 in this case
                - Formula: Let num = (n + 2^i) mod (2^m) #  mod is the modulo operator that represents remainder
                    i-th entry in finger table for a peer with id n and system parameter m 
                    is given by first peer at or in succession to "num" where num = (n + 2^i) mod (2^m)
                  
                - Let the peer circle look like 16 -> 32 -> 45 -> 80 -> 96 -> 112 -> 16
                  
                - for N = 80 and m = 7, finger table entries will be from i = 0 to 6
                    finger table entry i = 0,  num = (80 + 2^0) mod(2^7) = 81, next in succession = 96, ans = 96
                    finger table entry i = 1,  num = (80 + 2^1) mod(2^7) = 82, next in succession = 96, ans = 96
                    finger table entry i = 2,  num = (80 + 2^2) mod(2^7) = 84, next in succession = 96, ans = 96
                    finger table entry i = 3,  num = (80 + 2^3) mod(2^7) = 88, next in succession = 96, ans = 96
                    finger table entry i = 4,  num = (80 + 2^4) mod(2^7) = 96, next in succession = 96, ans = 96
                    finger table entry i = 5,  num = (80 + 2^5) mod(2^7) = 112, next in succession = 112, ans = 112
                    finger table entry i = 6,  num = (80 + 2^6) mod(2^7) = 16, next in succession = 16, ans = 16
                  
                - finger table as a dict  at peer 80: {0: 96, 1:96, 2:96, 3: 96, 4: 96, 5: 112, 6: 16}
    
    - How to place files on a ring in consistent hashing ?
        - SHA-1 applied to file name -> 160 bit string -> truncate it to m bits -> a file id , an integer between 0 to 2^m - 1
        - File is stored at first peer with an id at or clockwise to the file id, same logic as finger table pointers
        - Consistent Hashing Measurement
            - With K keys and N peers each peer stores O(K/N) keys 
            - Load at a single peer is < c*K/N where c is a constant with high probability, so good load balancing
        - So for example if our file id comes out to be 42, then it is stored at peer 45 which is 
        in the peer circle  16 -> 32 -> 45 -> 80 -> 96 -> 112 -> 16
          

    - Search in consistent hashing
        - Let us say we have a request to search a file with file id 42 at node 80 in the same peer circle
        - Search algorithm :
            - Check if the file exists at the system i.e for N=80, K=42 does not exist on 80
            - (Recursive Step 1) At node N send query for key K to largest successor/finger entry <= k
            - If none exist then send query to successor of N

            - In this example, N = 80, K = 42, peer_circle = 16 -> 32 -> 45 -> 80 -> 96 -> 112 -> 16
            - finger table as a dict  at peer 80: {0: 96, 1:96, 2:96, 3: 96, 4: 96, 5: 112, 6: 16}

            - so the largest finger table entry for N=80, which is to left of K=42, (in the circle) is 16
            - Now for 16 finger table is {0: 32, 1: 32, 2: 32, 3: 32, 4: 32, 5: 80, 6: 80} # calculated same as for N=80
            - Now 16 follows the same rule, forwards the request to nearest neighbor that is to left of 42, i.e. 32
            - Now at 32 the finger table is {0: 45, 1: 45, 2: 45, 3: 45, 4: 80, 5: 80, 6: 96} so it does not have any entry which is left of 42
            - so it passes on to its successor which N=45 and for K=42 file is stored at next greater peer id that is 45
            - This way we find the file
            - All these successive calls are RPCs or remote procedure calls

            - Whenever a query takes a hop from one node to another, the distance between the node and the peer with file reduces by half
            - This way searches are O(Log(N)), and inserts and deletes are based on searches so they are also O(Log(N))

    - The finger table may give wrong values if the peers have died or moved out because of churn because then the finger table itself may be inconsistent

    
    