Challenge in a distributed data center:

    - To build an efficient failure detector in a datacenter
    
    - Failure frequency:
        - The rate of failure of one machine is once every 10 years or 120 months 
        - If the data center has 120 machines, the failure rate is 1 machine per month
        - If the data center has 12000 machines the failure rate is once every 7.2 hours
        - So failures are a norm rather than exception
        - Results of failure: unintended data loss
        - Software failure detector
    - Example distributed system needing failure check
        - cloud data centres, replicated servers, distributed databases
    - Failure mitigation models
        - Crash stop/fail stop failure 
    - Group Membership Service
        - It maintains a membership list which is a list of all non faulty processes
        - Two components of Membership service: Failure detection and dissemination
        - All this happens over an unreliable network
        - The membership list is accessed by a variety of applications like gossip based apps.
        - Membership protocol aims to keep the membership protocol up to date as processes join, leave or crash
        - The membership list might be consistent forever (strongly consistent), weakly consistent (gossip style)
        - When a process fails, at least one working process should come to know about it and it should disseminate the news
        - Multiple process may find about the failure but at least one definitely should 

Failure Detectors:

    - One or more process should be aware if a crash occurs.
    - Frequency of failure increases linearly as number of nodes go up
    - Failure Detector desirable properties:
        - Completeness: each failure is eventually detected by a non faulty process
        - Accuracy: there is no mistake in detection, no false positives
        - Speed : Time to detect the first failure
        - Scale: Equal load on each member, avoid single point of failure
    - It is impossible to have 100% complete and 100% accuracy failure detector in lossy networks
    - We guarantee completeness but compromise on accuracy (probabilistic guarantee on accuracy)
    - Speed is the time taken to detect failure from the time it occurred, it should be as low as possible.
    - Scale: Multiple processes can fail in arbitrary manner (simultaneously) so failure detector should be robust
    - This is achieved by heartbeat which are incrementing sequence numbers
    
    -CENTRALIZED HEARTBEAT
        - All processes send heartbeat signals to a center managing process
        - If the center process does not receive heartbeat for sometime from a process, it marks it as failure
        - Single point of failure is the managing process, plus it is over loaded
    
    - RING HEARTBEAT
        - Processes are arranged in a virtual ring where each process recieves heartbeat from its left and right neighbor
        - This avoids hotspots but some failures may go undetected
        - When a process whose left and right neighbors have failed, reports both and by the team the
        left and right neighbors are brought back to life, if the process itself fails, then there is 
        no detection in the failure of the center process
        - Need to repair the ring
    
    - ALL-TO_ALL HEARTBEAT:
        - Every process sends heartbeat to every other process
        - The protocol is complete, if a process fails at least one non faulty process will come to know about it
        - High overhead of sending messages
        -If there is a slow process that receives heartbeat from other process after an interval,
        it will mark all other processes as failures. This means there is a high risk of false positives
        - So we plan to make the ALL_TO_ALL Heartbeat more robust
        
Gossip Style Membership

    - Every process randomly selects a group of B targets to gossip
    about their heartbeats every "T_gossip" seconds  
    - Every process maintains a state of process_id, heartbeat counter and local time.
    - 1 | 10353 | 65
    - 2 | 10467 | 67
    - 3 | 10483 | 69
    - 4 | 10489 | 70 (An example membership list on the process)
    - It is important every process has its own local time because this is an asynchronous system
    
    - When a process gets the membership list of another process, it 
    merges the new one in itself. 
        - It matches the process id and corresponding heartbeat counter
        - If the heartbeat counter of an incoming process is higher than what is stored in the process locally.
        - The it updates the row with new heartbeat counter and the current local time at the process
    
    - If a process has not recieved a heartbeat from a particular process
    for "T_fail" seconds then it marks it as failure, and then waits
    "T_cleanup" seconds to remove it from the membership list.
    
    - Typically "T_fail" and "T_cleanup" are similar in duration.
    - We need to wait a certain time after marking a process as failed because it may be
    possible that the process marked fail is part of membership list of another process
    - Waiting this much does ensure a low false positive rate.
    
    - So T_fail and T_cleanup help with maintaining low false positive rate 
    - T_gossip helps you to trade off between bandwidth used by this application

Optimal Failure Detector

    - Guarantee completeness
    - Accuracy - PM(T) -> Probability of mistake in time T
    - Speed: T Time units
    
    ALL TO ALL HEARTBEATING WITHOUT GOSSIP:
        - Let T be the time gap between sending hearbeat for each process
        - Let N be the total number of processes in the system
        - Load for 1 process is N/T because each process is sending its membership 
        list to every other process
        
    ALL TO ALL HEARTBEATING WITH GOSSIP:
        - In Gossip, every T_gossip time units, O(N) gossip messages are sent out
        - T = log(N) * T_gossip # By gossip protocol design
        - Load = N/T_gossip = N*log(N)/ T
    
    What is the optimal?
        - Given :
            - T - Time to first failure
            - PM(T) - Probability of mistake
            - p_ml - Independent message loss probability
        
        - L* = (log(PM(T))/log(p_ml)) /T # can be shown, this is optimal load
        - We see optimal load is independent of scale.
        - All to all heartbeat (with or without gossip) is sub optimal because it depends on N
     
    Optimal Probablistic Failure Detector
        - SWIM : Scalable Weakly consistent Infection style Membership protocol
        - We use pinging instead of heartbeating
        - Process p_i run a protocol every T time units called protocol period
        - In the beginning it picks another process p_j at random and sends it a ping message
        - If p_j receives a ping message it responds back with an ACK message
        - If p_i reveives an ACK from p_j it does nothing more in the protocol period
        - If p_i does not hear back because ping is dropped or ACK is dropped, it tries
        to p_j again by using indirect path.
        - p_i sends indirect pings to "K" other random processes, these indirect
        processes send a direct ping to p_j
        - If p_j recieves an ping from any other process, it replies back with
        an ACK.
        - Any indirectly pinged process (1 out k) if it gets an ACK from p_j it responds
        back with an indirect ACK.
        - If p_i receives a direct or indirect ACK from p_j in the protocol period then
        it is happy, else it marks p_j as a failure.
        
        - p_i is giving p_j a second chance to respond.
        - p_i is not relying on its direct connection to p_j, it explores randomly
        available options.
        - Temporal chance to p_j using a second ping
        - Spatial chance to p_j using indirect paths
        
    SWIM vs HeartBeat:
        - For a fixed false positive rate and message loss rate
        - For a low process load, detection time can be high in ALL TO ALL
        - For a low deteciton time, process load can be high in ALL TO ALL
        - SWIM has constant detection time and constant load per process in expectation
        
    - SWIM ANALYSIS:
        - First Detection time: (e/(e-1)) * protocol_period , on expectation, constant
        - Process Load : Each process sends 1 + (at the max K) pings per Protocol period, so it is constant
        - False Positive rate: Tunable by "K" parameter
        - Completeness: Determinsitic time bound With (O(Nlog(N))) with high probability.
        - Probability of Mistake:
            - depends on -K
            - depends on p_ml and probability of multiple failure
         
        - Probability of being pinged in T = 1 - (1 - N^-1)^(N-1) = 1 - e^-1 as N -> inf
        - E[T] = 1 - e^-1
        - Completeness:
            - Once a process fails at least one process will ping it, and mark it as fail
            - when you pick a membership element you pick next element in a linear fashion.
            - when you reach the end of membership list, you create a random permutation of the membership list
            - Preserves the Failure Detection properties
            
    - Dissemination and Suspicion:
        - Options for dissemination
            - Hardware Multicast: 
                - cons: unreliable, multiple simultaneous multicast
                - If multiple messages detect failure, they start multiple multicasts
            - Point to Point:
                - Expensive
            - Zero Extra Message :
                - Piggyback on SWIM Pings, ACKs, Indirect Pings and Indirect ACKs.
                - Infection style dissemination
        
        - Infection style dissemination with SWIM
            - After k*log(N) protocol periods, N^(-2k-2) processes would not have heard
            about the update, (this defines weak consistency)
            - Maintain a buffer of recently joined/evicted processes
                - piggyback from this buffer
                - remove least recently used updates
                - buffer elements are garbage collected after a while
        
        
        - Suspicion Mechanism:
            - Some process may be perturbed meaning it has high message loss rate around it
            - Packet loss forms congestion
            - Indirect pinging may not solve the problem as paths around the perturbed process may be congested
            - Idea is to suspect a message as failed before declaring it as failed
            
        - State Machine Example
            - p_i maintains a state machine for another process p_j where p_j is a process in its membership list
            - by default p_j is alive
            - if failure detector detects p_j to be failed, it moves process p_j to the state SUSPECTED
            - it also disseminates message via SWIM piggyback message that p_j is suspected to fail
            - this state sustains for a while till a timeout, and after the timeout the process p_j is marked as fail
            - then it is disseminated that the process p_j has failed
            - while the state is suspected for process p_j if p_i recieves a direct ping from p_j
            or message from someone that p_j is alive, p_i marks p_j alive 
            - one of the problem is p_j can be going ON and OFF multiple times in its lifecycle
        
        - Dealing with multiple ON and OFF processes in failure detector:
            - There is a per process incarnation number
            - Incarnation number for p_i can be updated only by p_i when it receives a SUSPECT p_i message, i.e. someone
            is suspecting p_i to have failed.
            - It then increments its incarnation number and sends ALIVE p_i message to all
            - Similar to DSDV protocol
            - Higher or same incarnation number notification override the lower incarnation number information
            - Failed message for any process overrides any incarnation number
            
            

           
                
            
    
    
    
     