Consensus Problem

    - Some vendors say they have five 9s of reliability which is 99.999 % reliability
        but not 100 %, because of impossibility of consensus
      
Common distributed systems problems
  
    - Ensure all processes receive updates in the same order as each other (RELIABLE MULTICAST)
    - Actively maintain membership list at each process, in the event of joining, leaving or failing of a process (MEMBERSHIP/FAILURE DETECTION)
    - Elect a leader among them adn let everyone in the group know about it (LEADER ELECTION)
    - Ensure mutually exclusive access to critical resources like a file (MUTUAL EXCLUSION)

What is common in these problems?
      
    - The processes in the distributed system are attempting to coordinate among each other    and reach on agreement on value of something
      - The something could be
        - ordering of messages
        - up/down status of a suspected failed process
        - leader election
        - access to critical resource
    - All of these are consensus problem
    
    
Formal consensus statement

    - Given N processes such that
        - each process p has an input variable xp (either 0 or 1) and output variable yp (either 0 or 1)
    - Consensus problem: Design a protocol so that at the end either
        - All processes set their output variables to 0 (all-0's)
        - All processes set their output variables to 1 (all-1's)
    - Every process contributes a value
        - Once a decision is made per process it cannot be changed because upstream systems depend on it
    - Constraints
        - Validity: Rule of majority, if everyone proposes same value then that's what is decided
        - Integrity: decided value must have been proposed by some process
        - Non triviality: there is at least one initial system state that leads to each of the all-0's or all-1's outcomes
    - Problems similar to consensus (harder or equivalent to consensus)
        - Perfect Failure Detection
        - Leader election
        - Agreement

Synchronous distributed system model

    - Each message is received with bounded time (a global bound)
    - Drift of each process's clock has a known bound
    - Each step in a process takes a bounded "time" i.e. lower_bound < time < upper_bound
    - Example: A collection of proccessors connected by a communication bus

Asynchronous distributed system model

    - No bounds on process execution
    - Drift rate of clock is arbitrary
    - No bound on message transmission delays
    - A protocol for asynchronous distributed system will work for synchronous one but not vice versa

Consensus in Synchronous systems

    - Know the system model and its implications
    - Failures in synchronous systems are crash-stops (no more instruction executed after the failure)
    - At most f processes crash (f can be equal to N where N is total number of processes in system)
    - All processes are synchronized and operate in rounds of time
    - algorithm proceeds till f+1 rounds using reliable communication to all members (some variant of TCP)
    - Values(r, i) : represents set of proposed values know to process p_i at the beginning of round r

    - Example run of consensus at process p_i
    - At the beginning of protocol i.e round 0, values(r, i) array is empty, Values(0, i) = {}
        - At the beginning of first round, you include value contributed by the process p_i, Values(1, i) = {v_i} # v_i is value contributed by process p_i
        - for round 1 to f + 1:
            - p_i multicasts all new values received since the last round (loop through all processes and send the message)
            - In the first round it will be the value v_i for the process p_i
            - But in subsequent rounds you may receive other values from other processes and you multicast these new value received in just the last round
            - you wait to receive value from the other processes
            - you set your value for r+1th round same as that was for rth round (this is important see Integrity constraint)
            - for each v_j received you update Values(r+1, i) with v_j
        - After f + 1 rounds done at each process, you simply look at your values array and pick the minimum value from it
        - Set your processes's output variable to this minimum value

    - Proof by contradiction for consensus for synchronous systems
        - Assume two non fauly processes say p_i and p_j differ in their final set of values after f+1 rounds
        - Assume p_i possesses a value v that p_j does not possess
        - p_i must have received value v in the last round otherwise it would have sent v to p_j in that last round
        - So in the last round a third process p_k must have sent v to p_i but then crashed before sending v to p_j
        - Similarly one round prior to last round a fourth process sending v must have crashed otherwise 
          both p_k and p_j must have received v
        - Proceeding in this way we infer at least one crash in each of the preceeding rounds
        - This means a total of f+1 crashes while we have assumes at most f crashes that occur
        - Hence proved by contradiction

PAXOS (Invented by Leslie Lamport)

    - Consensus is impossible to solve in asynchronous systems because it is impossible to distinguish
    a failed process from one which runs very slow, hence rest of the alive process may stay ambivalent(forever) when it comes to
    deciding (FLP Proof : Fischer, Lynch and Patterson)
    - PAXOS provides safety and eventual liveness, used by zookeeper, Google Chubby
    - Safety: Consensus is not violated, integrity is maintained, no two non faulty processes decide different values
    - Liveness: Processes actually reach on agreement with high probability
    - No guarantee on liveness time bound 
    
    - PAXOS simplified
        - Works in asynchronous round
        - Time synchronization is not required
        - If you are in round j and hear a message from round j + 1, abort everything and move over to round j + 1
        - Using timeouts may be pessimistic
        
        - Three phases of a round, each is asynchronous
            - Election : A leader is elcted
            - Bill : Leader proposes a value, processes acknowledge
            - Law: Leader multicasts final value

        - Election
            - Potential leader chooses a unique ballot id, higher than seen anything so far
            - Sends to all processes
            - Process wait, respond once to highest ballot id
                - Each process votes exactly once to the highest ballet id it has seen so far
                - If potential leader sees a higher ballot id, it cant be a leader, it rejects itself
                - Paxos tolerant to multiple leaders but this analysis is about single leader paxos only
                - Processes write to disk the received ballot ID 

            - If a process has in a previous round decided on a value v_, it includes value v_ in its response
            - If majority respond OK then the potential leader becomes the real leader
            - If things go right, a round cannot have more than two leaders because each process votes at most once
            - Its possible no one reaches a majority, then you start next round again with election phase

        - Bill
            - The leader sends a proposed value v to all
            - if some process already decided in a previous round and sent the leader v* then leader is supposed to send v*
            - Recipients log on disk, Respond OK
        
        - Law 
            - If leader hears a majority of OKs it lets everyone know of its decision
            - Reciepients receive decision, log it on disk and update their decision variables
        
        - Point of no return when consensus is reached is Bill phase
        - Safety guarantee
            - if some round has a majority i.e. quorum hearing proposed value v_ and accepting it, then subsequently at each round 
                - either the round choose v_ as decision
                - round fails

            - Proof
                - Potential leader waits for majority of OKs in Phase 1
                - At least one will contain v_ (because two majorities or quorums always intersect)
                - It will choose to send v_ in phase 2
            - Success requires a majority or quorum and any two majorities intersect

        - Things that can go wrong
            - Majority does not include a failed process
            - leader fails
            - Messages get dropped
            - quorums may not be reached
̐
        
        