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
    
    - Fully distributed  
  