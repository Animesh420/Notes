- Multicast is a message that needs to be sent out in a group of processes
- Broadcast is a message sent to all processes anywhere
- Unicast is a message sent from one sender process to one receiver process
- Multicast examples:
    -  Cassandra, Online scoreboards like ESPN, Air Traffic Control system, stock sxchanges
    - Multicast needs to be reliable and ordered
  
FIFO Multicast ordering:

    1. Multicast from each sender are received in the order they are sent at all receivers
    2. If a correct process issues multicast (g, m) to group g and then multicast (g, mx) then every
    correct process that delivers mx would already have delivered m.
    3. We dont worry about multicast from different senders

Causal Multicast ordering:

    1. Multicasts whose "send" events are causally related must be received in the same causality obeying order at all receivers
    2. If multicast(g, m) happens before a multicast(g, m_) then any correct process that delivers m_ would already have delivered m. (happens before is from Lamport Timestamps)

Total ordering Multicast ordering

    1. This ensures all receivers receive all multicasts in same order
    2. If a process P delivers message m before  m_ then any other correct process P_ that delivers m_ w

Maintaining FIFO Ordering Multicasts:

    - each receiver in a group maintains a per sender sequence number 
    - Let there be N processes in the system
    - Process p_i maintains a vector of sequence number p_i which is a vector of length n  initially all zeros
    - p_i[j] is the latest sequence number p_i has received from p_j.
    
    Sending multicast from process p_j:
        - set p_j[j] += 1
        - Include this new p_j[j] in mutlicast message as its sequence number

    Receive multicast from process p_j:
        - If p_i receives multicast from p_j with sequence number S in message
            - if s == p_i[j] + 1
                - deliver the message to application (process the received message)
                - set p_i[j] = p_i[j] + 1
            - else:
                - buffer this multicast unitl above condition is True

Maintaining Total Ordering Multicasts:

    - Sequencer based approach
        - Special process elected as leader or sequence
        - Sending a message from process p_i
            - Sends multicast message M to a group and sequencer
            - Sequencer maintains a global sequence number S (initially zero)
            - When it receives a mutlicast message M, it sets S = S + 1 and multicast <M, S>
        - Receiving a multicast at process p_i:
            - p_i matains a local received global sequence number s_i, initially zero
            - if p_i receives a multicast M from p_j, it buffers it until
                - p_i receives <M, S(M)> from sequencer
                - s_i + 1 == S(M)
            - When these two conditions are met, then it delivers the message to application
            and sets s_i = s_i + 1

Causal Ordering Multicasts:

    - Similar to FIFO each receiver maintains a vector of per sender sequence number
    - Let there be N process oin the system
    - for a process <p_i>, with a local vector p_i[1..N]
        - p_i[j] is the latest sequence number p_i has received from p_j

    - Send a multicast at process p_j
        - set p_j[j] = p_j[j] + 1
        - include new entire p_j[1..N] in multicast message as its sequence number
    
    - Receive multicast at process p_i:
        - If p_i receives a multicast form p_j with vector M[1..N], buffer it unitl 
        following both are satisfied
            - Message is the next one p_i is expecting from p_j
                - M[j] = p_i[j] + 1
            - All multicasts anywhere in the group which happened before M have been
            received at p_i, i.e.
                - For all k != j, M[k] <= p_i[k] (receiver satisfies causality)
        - Once these two conditions are met deliver M to application and set p_i[j] = M[j]

- Ordering can be also implemented as hybrid of two approaches, causal + total or fifo + total

Relaible Multicasts

    - Reliable multicast lossely refers that every process in the group receives all multicasts
    - Can implement Reliable-FIFO, Reliable-Casual or Reliable-Total or Reliable-Hybrid protocols
    - When process failures happen definition becomes
        - all correct (i.e. non fauly) processes in thr group receives all mutlicasts
    - Reliable multicast says that all multicast that are sent to group are either received at all correct processes or at None
    - Reliable unicast protocol : TCP 
    - Inefficient reliable protocol
        - When a sender sends a multicast message to a group of N processes, sequentially
        each process in the group starts to send the message to all other process sequentially too
        - The process in the group send message to all other proceseses if they have received the message for the first time   
        - Each process helps the sender to ensure reliability i.e. if one non faulty process 
        receives a message then it is guaranteed that all non faulty processes would have received 
        the message


Virtual Synchrony or view synchrony

    - Attempts to preserve multicast ordering and reliability inspite of failures
    - Combines a membership protocol with a multicast protocol
    - Systems that implement it like Isis are used in NYSE, Swiss Stock Exchange
    
    Views
    - Each process maintains a membership list called view
    - An update to membership list is called view change, (process join, leave or failure)
    - Virtual synchrony guarantees that all view changes are delivered in the same order at all correct processes
    - Views may be delivered at different physical times at processes but they are delivered in the same order
    - Examples
        - If a correct process P1 got view changes like (in order)
            1. {P1} : P1 joins
            2. {P1, P2, P3}: P2 and P3 joins
            3. {P1, P2} : P3 leaves
            4. {P1, P2, P4}: P4 joins
        - Then for the next correct process P2 the view changes will be
            1. {P1, P2, P3}: P2 and P3 joins
            2. {P1, P2} : P3 leaves
            3. {P1, P2, P4}: P4 joins

    Vsync Multicasts:
        - A mutlicast M is said to be "delivered in a view V at process P_i" if
            - P_i receives view V, and then sometime before P_i receives the next view it delivers multicast M
        - Virtual synchrony ensures that set of multicasts delivered in a given view is the same set at all correct processes that were in the view
            - What happens in a view stays in that view
            - If a view has processes say P1, P2, P3, the set of multicast received at P2 are same as the set of multicast received at P1
        - The sender of the multicast message also belongs to that view
        - If a process P_i does not deliver a multicast M in view V while other processes in the view V delivered M in V, 
        then P_i will be forcibly removed from the next view delivered after V at the other processes

