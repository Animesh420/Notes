- 0-30
- Distributed Systems
    - A set of cooperating computers that communicate over a network to work
    coherently. Eg: storage for big websites, P2P, map reduce
    - Gains from Distributed system
        - Parallelism
        - Fault Tolerance
        - Some problems have natural affinity to use distributed systems
        - Security and isolation
    - Difficulties with Distributed system
        - Failures are difficult to detect, (Network or nodes)
        - Complicated Concurrent Programming problems
        - Performance
    - Infrastructure for distributed systems:
        - Storage : Example: HDFS (Distributed File system)
        - Communications : Example: RPC
        - Computations : Example : Map Reduce (Computation system)
    - Ideal to have non distributed abstractions that hide underlying distributed architecture
    - Implementation
        - RPC
        - Threads (way of structuring concurrent operations)
        - Concurrency control
    - Performance in distributed systems
        - Scalable speedup
        - Adding more machines decreases problem solving time
    - 30-60
    - Fault Tolerance
        - Constant failures in distributed systems
        - Criteria for fault tolerance
            - Availability till a certain set of failures
            -  Recoverability : The system can get going again
          
        - Some tools for fault tolerance
            - Non-Volatile storage: Costly to write multiple times, but important for recoverability
            - Replication: Management of replicated copies is tricky, effort is put in to maintain synchronising
    - Consistency
        - Example: Key value distributed storage applications
          - Put(key, value) and Get(key) are main operations
          - For performance and fault tolerance we have more than one copy of data floating around
          - For a replicated system, there may be different values of key value in different systems.
          - Strong consistency is a very expensive spec to implement, weak consistency is easier
          - In a strong consistency case, you need a lot of communication to maintain correct state everywhere
          - We need replicas to have independent failure probabilities, so replicase are usually put in a distant location
          - In this case communication latency is quite high to maintain strong consistency
    
    - Example of map reduce
        - Word count 
          - Map stage splits the sentence into words and emit key value tuple of (word, 1)
          - Reduce stage aggregates the words by the count emitted from all map outputs
    
        - Map stage produces output that is available for each key
        - Before starting any reduce stage,  all map stage outputs should have been generated
        - Map Reduce reads and writes to Network File System (GFS - Google File System)
        - GFS splits data into 64kb chunks distributed uniformly over multiple servers
        - To run map reduce you need a network file system, essential for good throughput
        -  A simulation of how efficiently map reduce worked
            - A master process took care of assigning map tasks to different inputs
            - Inputs to map tasks are usually files which are stored in servers under GFS
            - The master process, cleverly figures out which file is in which server under GFS
            - The process of running a map task is executed on the same server which has the input
            - Thus, storage and computation happen on the same server in this case to reduce network latency and 
            run as if it were a local access event with high probability.
              
            - Sharing the output of map phase with different reducers is the expensive part where the map output needs to
            be grouped by a common key and passed on to reducer over a network which is a costly step.
              
            - Modern systems use stream based approach to reduce the network latency
            - Modern data centers have better network throughput due to faster network speeds available
    

    
    