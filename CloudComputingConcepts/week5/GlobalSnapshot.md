- Global Snapshot
    - Problem statement: Record a global snapshot (state for each process and state for each channel)
    - System Model Assumptions
        - N processes in system
        - There are two uni directional communication channels between each ordered process pair
            - P_i -> P_j and P_j -> P_i
        - Communication channels are FIFO ordered
        - Communication channels are represented by C_ki (channel from k to i)
            - This channel is incoming channel for i
            - This channel is outgoing channel for k
        - No Failure
        - All messages arrive intact and are not duplicated
    
    - Requirements
        - Snapshot should not interfere with normal application actions, and it should not interfere applications to stop
        sending messages
          
        - Each process should be able to record its own state
            - Process state, heap, registers, program counter etc
        - Global state is collected in a distributed manner
        - Any process may initiate the snapshot
    
    - Algorithm (Chandy Lamport Global Snapshot Algorithm)
        - Initiator behavior
            - Let P_i be the initiator process
            - P_i records its own state first
            - P_i sends a special message called "marker" message to all other processes (for j = 1:N except i) on outgoing channels like C_ij
            - These messages are sent like application message in channels, but they don't have application specific information
            - They arrive in communication networks, as FIFO
            - P_i turns on recording the messages of all the incoming channels(C_ji where j != i) at P_i. 
    
        - Receiver Behavior: When P_i receives a marker message on an incoming channel C_ki
            - Let P_i be a receiver process and P_k be the initiator process and C_ki be the channel of communication
            - When P_I receives a marker message
                - If this is the first time P_i is seeing this message
                    - It records its own state 
                    - Marks the state of channel C_ki (incoming channel to i from k) as empty
    
                - for all "m"  processes except P_k and P_i
                    P_i sends out a marker message on outgoing channel C_im (outgoing channel from i to m)
                  
                - P_i starts recording the incoming messages on each of its incoming channels (C_pi, channel from p to i, incoming for i)
            
            - When P_I has already seen a marker message that it receives from a channel k:
                - Mark the state of channel C_ki(channel from k to i, incoming for i)
                as all the message that have arrived at it since recording was turned on for C_ki
                - It stops recording the state on the incoming channel C_ki
              
            - The state of a channel is snapshotted only at the process that is at the receiving end of the channel
              
        - Algorithm ends:
            - When all processes have received a marker message
            - When all processes have received a marker on all N-1 incoming channels at each
            - If needed a central server collects all these partial state pieces to obtain the full global snapshot
    
- Correctness of Chandy Lamport Algorithm
    - Cut is a time point at each process or at each channel.
        - Everything before the time point is considered to be in the cur and everything after the time point is considered after the cut
    - Consistent cut
        - a cut that obeys causality
        - For each pair of events E and F and F happened before E and E is in the cut, this implies that F is also in the cut.
    - Chandy Lammport Algorithm always creates consistent cuts, this is the reason of correctness of Chandy Lamport Algorithm
    
- Safety and Livenss: (important for correctness in distributed system)
    - Liveness: Something good will happen eventually
        - Example 
          - A distributed computation will terminate
            - Completeness in failure detector
            - All process eventually decide 
    - Safety; Something bad will never happen
        - Example
            - There is no deadlock in a distributed system
            - No object is orphaned in a distributed system
            - Accuracy in failure detectors
            - No two process decide on different values
    - Guaranteeing both is difficult
    - Distributed system moves from one global state to another global state via causal steps
    - Liveness wrt a Propery P1 in a given state S means, 
        - S satisfies P1 (OR)
        - there is some causal path of global states from S to S' where S' satisfies P1
    
    - Safety wrt a Propert P1 in a given state S means
        - S satisfies P1 and all global states S' reachable from S via causal paths also satisfy P1
    - Chandy Lamport Algo, can be used to detect global properties that are stable
        - Stable : Once true, stays true forever afterwards
    - Stable liveness property: computation has terminated
    - Stable Non-Safety property: There is a deadlock, or an object is orphaned
    - All stable global properties can be detected using the Chandy Lamport algorithm due to its causal correctness
    
                        
    