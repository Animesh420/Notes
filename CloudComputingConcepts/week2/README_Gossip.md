## Building blocks of distributed systems
Gossip or Epidemic protocols
- Multi-cast Problem: 
    - In a group of processes or nodes, in a distributed network when a node has new information
    how should it disseminate this information to the other nodes in the network.
    - Multi cast is different from broadcast as broad cast share to every other node,
    multi cast sends to specific nodes
    - Problems:
        - Nodes may crash
        - Packets may be dropped
        - Large number of recipient nodes (scalability problem)
            - Overhead per node should not gorw very quickly as the number of nodes increases rapidly
       
     - Typically sits in the application layer (talks to underlying network layer like IP Multicast)
     - IP Multicast is available in router but not attractive as it may not be enabled by default
     
     - Brute Force:
        - Centralized approach:
            - Sender sends  each recipient one by one in a loop
            - Overhead on sender is high
            - Sender is single point of failure
            - Latency for recipient is high in case of many recipients receiving the message in this sequential approach
    - Tree Based Multicast approach:
        - Build spanning tree among the processes of the multicast group
        - A balanced Spanning Tree provides O(height of tree) time for receivers to receive messages
        unlike O(number of recipients) in Centralized approach
        - Any node that has children, if fails, process needs to rebuild the spanning tree,
        which is a costly operation, failures are norm rather than exception
        - Use spanning tree to disseminate multicasts
        - Use either ACKs(acknowledgments) or NACKs(Negative ACKs)
        - Example: SRM (Scalable Reliable Multicast), RMTP(Reliable Multicast Transport Problem)
        - The protocols have O(N) ( where N is size of network ) NACK and ACK overhead.
        - Hence this is not a scalable protocol to live with
     
     - Gossip Protocol
        - Sender periodically selects "B" targets at random and sends them 
        copy of multicast message using what is known as Gossip message. This transmission
        uses UDP (unreliable but fast)
        - B: This is called Gossip Fanout or Gossip Parameter
        - These nodes are picked with replacement, it is possible that one node is picked twice
        by the sender.
        - The target is said to be "infected" by the gossip and it acts as a sender.
        - An infected node periodically sends out B copies of message to a randomly selected target.
        - Gossip protocol is not synchronized each node has its own routine of settling routines
        - This is a push based Gossip protocol
        - If you have multiple messages, you can gossip a group of messages based on randomness,
        importance or some other criteria.
        - Alternative, pull based protocol is possible where each node is polling other nodes
        if they have received a new multicast message since the last time they spoke.

    - Analysis of Gossip Protocol:
        - Claims:
            - Light Weight
            - Spreads multi cast quickly
            - is highly fault tolerant
        
        - Derived from branch of epidemiology
        - Population of n+1 individuals mixing homogeneously
        - Probability of contact : b
        - At any time and individual is either uninfected or infected.
        - Let y_t denote the infected individual at time t and x_t denote the uninfected
        individual at time t.
        - y_0 = 1 and x_0 = n
        - x_t + y_t = n + 1
        - When an uninfected individual comes in contact with an infected individual,
        it get infected and stays infected.
        - Continuous time process
        - rate of change of uninfected:
            (dx/dt) = - b * x_t * y_t ## differential equation
            - This is negative because number of uninfected is decreasing always.
            - x_t * y_t is total number of possible pairs of infected and uninfected people
            - If there are 3 infected people and 2 uninfected people, total 6 pairs are possible (6 = 3 * 2)
            - Out of these x_t * y_t, b is the probability of contact of any pair so we multiply it with b.
            
            - Solution: x = (n * (n + 1)) / (n + exp(b * (n+1) * t)) --> Eq_x
            - Solution: y = (n + 1) / (1 + n * exp(-b * (n+1) * t))  --> Eq_y
        
        - How gossip spreads fairly fast?
            
            - The value of epidemic parameter b = B/n
            - The probability that an infected node picks an uninfected node out of
            n nodes where it always selects B nodes (Gossip fanout) is B/n
            - y = (n + 1) - (1/ n^(cB - 2)) , substitute, t = clog(n) --> Eq_y_*
                - where B = Gossip Fanout
                - t = c* log(n) in Eq_y
            - as n increases, y becomes n+1 very fast as second time dies quickly.
            - Since c*log(n) round has happened, each node sends maximum c * B * log(n) message
            - So push based gossip protocol
                - Has weight per node as CBlog(n) which makes it light weight
                - Quick spread, as the second term in Eq_y_* dies very quickly.
                - In C log(n) rounds y tends to be n+1 which is entire population so it is low latency as well
                
            - Fault Tolerance:
                - packet loss:
                    - 50% packet loss, replace B by B/2
                    - To achieve same reliability as 0% need to wait 2 * c * log(n) round, which is still cheap
                - node failure:
                    - 50% of nodes fail, analyze with n replaced with n/2 and b replaced with B/2
                    - Same strategy wait twice.
                - once a gossip has infected few nodes of the system, it is very hard to die of
            
            - Pull Gossip Protocol:
                - To reach at least n/2 nodes it takes O(log(n)) rounds 
                - After that pull is faster than push
                - After the ith round let p_(i) be the fraction of non infected nodes and B be the number of nodes selected by gossip everytime
                - p_(i+1) = p_i * (p_i)^B = (p_i)^(B+1)
                - Probability that a node stays uninfected at the end of i+1 th round, is probability that
                it was uninfected in the beginning (p_i) and it stays uninfected even when the
                protocol picks B nodes.(p_i ^ B)
            - Gossip implementations:
                - AWS EC2 and S3, Cassandra
                

