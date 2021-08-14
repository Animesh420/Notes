- P2P systems are distributed systems that seriously focused on scalability with respect to number of nodes
- P2P techniques are common in cloud computing system, Key Value stores like cassandra dn Riak use Chord(a P2P system)
p2p hasing
-  Widely deployed P2P systems
    - Napster
    - Gnutella
    - Fasttrack
    - Bittorrent
- P2P Systems with Provable properties
    - Chord
    - Pastry
    - Kelips    

- Napster:
  
    - Napster is a large P2P distributed system
    - Two main components of Napster are Napster Clients and Napster Server
    - Each user runs a Napster Client on his/her system
    - When you upload a file to Napster it does not go anywhere, it exists locally on the system
    - There are Napster servers which store directory information, file information, client information
    - The Napster serves don't store files they store directory information.
    - When a client connects to server, it uploads information about the files that it wants to share with the servers
    - The server maintains a list of tuples, <ip address, port number, file name, keywords to file> etc.
    - When another client wants to search for a particular file, the servers in Napster talk to each other and search their directories for the key word provided by client
    - Then the servers return a list of available clients  (ip_address, port number) to the querying client
    - Querying client pings each host, to check which has the best transfer rate and fetches the file from the one.
    - All communications happen via TCP (reliable transport layer transmission control protocol)
 
 - How do peers join the P2P servers?
    
    - Peers send a http request to a well know url, for that P2P service
    - Message is routed to another well known server called Introducer, which keeps track of some recently joined nodes in p2p systems
    - Introducer initializes new peer's neighbor table
 
 - Problems with Napster:
    - Servers are centralized point of failure and congestion, the security of system is less
 
 - GNutella:
    
    - Fully distributed peer to peer system
    - No specialized servers like Napster to cater to clients
    - Each peer (same as client in Napster) acts as a servent ( client + server )
    - Peers like in napster store their own file, files do not go anywhere
    - Peers store what is called peer pointers, which is a tuple of (ip address and port) and thus can send the peer
    messages over TCP
    - This creates a graph among peers called overlay graph
    - Gnutella has 5 main message types
        - Query - search
        - QueryHit - response to query
        - Ping - to probe network for other peers
        - Pong - to reply to ping, with address and bandwidth of the target peer  
        - Push - to initiate file transfer
    - All fields except IP address are in little endian format, bits with less significance are stored at
    lower address byte
      
    - Structure of message in GNutella:
        - Descriptor ID : ID of transaction unique in the system
        - Payload Descriptor: Type of payload, 00 -> Ping, 01 -> Pong, 40 -> Push, 80 -> Query, 81 -> Queryhit
        - TTL : Decremented at each hop, normal value is 7-10
        - Hops: Incremented at each hop (never used)
        - Payload Length : Number of bytes of message following the header (all fields above)
    
    - Query Message:
        - Minimum speed | search criteria (present in payload)
        - A query message is flood out to all neighboring peers, and they propagate it further to all the peer child
          except the peer from which the message came
        - When a query message reaches TTL 0 it dies out i.e. it is not forwarded again.
        - Try to flood query messages to a large portion of the peer network
    
    - Query Hit
        - Payload
            - Num hits: no of files that match
            - Port & Ip address: Port and IP address of the responding peer
            - (fileindex, filename, size) : File metadata for each of the matched files
            - servent id: a unique identifier of the responder, may be used by the push message but not here
    
        - Query hits are reverse routed, it sends the message to peer from which it received the message
        - To avoid duplicate transmission each peer maintains a list of recently sent messages
        - The query is forwarded to all neighbors except the neighbor from which you have received it
        - Each query is forwarded only once
        - Duplicates with same descriptor id are dropped
        - The overlay graph may change because of peers leaving, if a peer receives a queryHit from a peer to which
        it has not sent a query message, it drops it. This may also happen if the sent message is not in the list
        of a recently sent message of the peer
        - When the querying peer receives the query hit message, the response is shown to client (on the querying peer) and download starts
        - The client sends  HTTP Get request to the responding peer message to download the file with a Keep Alive connection
        - The responding peer respond by file blocks, the file transfer is partial.
        - In case when the responding peer is behind the firewall, the requesting peer sends its ip address and firewall.
        - The responding peer pushes the file to the requesting peer in this case
        - In the case when both peers are behind firewall nutella gives up
    
    - Ping
        - No Payload
        - Message sent by peer to know its immediate neighbors
        - TTL is much smaller like 2-3
    - Pong
        - Response to Ping
        - Contains IP address and port number of responding peer 
        - Also has information about Number of files shared and number of KB shared
        - Ping and Pong are needed because P2P systems have a lot of churn, many peers joining and leaving
        - So it is important to periodically refresh the list of nearby peers to make sure one has the right picture
        - Periodic ping pong to continuously refresh its neighbor list
    - GNutella conclusion, drawback
        - List size at peer is specified by user, GNutella is found to follow power law distribution
        - P(#links = L) = L ^ -k (k is a constant)
        - Large traffic due to ping and pong
        - Ways to reduce frequency of pings and pongs: Multiples, cache results, cache query and query hit messages
        - Can use a central server to act as a proxy for low bandwidth servers
        - Freeloaders possess the challenge of over burdening a P2P system
        
        
    
        
    
    
        
    
  