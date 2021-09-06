- Time synchronization 
    - It is required for both correctness and fairness
    - Time is managed by system clock on the motherboard.
    
    - Let us say in a cloud flight management system, there are two servers
        - Server A receives a client request to purchase a ticket using local clock 9h:15m:32.45s
        - Server A purchases the ticket replies OK to client, this was the last seat on the flight
        - Server A tells server B to mark the flight as full, and Server B logs the flight is full
        at Server B's local time which is 9h:10m:10.11s
          
        - A third server, server C checks the logs of servers A and B, and finds out that the ticket was
        purchased (Server A timestamp) after the flight was marked full (Server B timestamp). It makes incorrect
          assumptions about the process and leads to chaos
          
    - In an asynchronous distributed world, each process has its own time clock.
        - In processors within one server or workstation they all share a system clock
    - In a distributed setup, each process within a single system can have ordered timestamps because they refer
    to the same clock. However, we also need to know the time order of events across different processes to understand
      the system as a whole.
      
    - Terms in clock
        - Clock skew: relative difference in clock values of two processes
            - Like distance between two vehicle on the road
        - Clock drift: relative difference in clock frequencies of two processes
            - Like difference in speeds between two vehicles on the road
    
        - A non-zero Clock Skew implies clocks are not synchronized 
        - A non-zero Clock Drift implies clock skew will increase eventually
    
    - How often to synchronize clocks
        - MDR : Maximum Drift Rate of a clock
        - MDR is defined relative to Coordinated Universal Time, UTC which is maintained by atomic clocks
        - MDR of a process depends on the environment
        - Max drift rate of two clocks with similar MDR is 2 * MDR
        - Given a maximum acceptable skew M  between any pair of clocks, need to synchronise it evey
            - t = M / (2 * MDR) ( time = distance / speed)
    
    - External synchronization
        - Each process C(i) clock is synchronized wrt an external well known time source S (like UTC or atomic clocks)
        - A bound D is defined such that abs(C(i) - S) < D at all times
        - Algorithms that achieve this: Cristian's Algorithm, NTP
    
    - Internal Synchronization
        - Every pair of processes in group have clocks with time bound D
        - abs(C(i) - C(j)) < D
        - Eg. Berkeley Algorithm
    
    - External Synchronization with D >= Internal Synchronization with 2 * D
    - Internal Synchronization does not imply External Synchronization
    