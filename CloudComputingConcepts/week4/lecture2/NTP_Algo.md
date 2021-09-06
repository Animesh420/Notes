- NTP (Network Time Protocol)
    - NTP servers are organized in a tree
    - Each client can be leaf of the tree
    - Each node synchronizes with its tree parent
    
- Workflow
    - A child (process) talks to the parent server saying it wants to synchronize time
    - The parent sends a message called MESSAGE1 with its local time as ts1
    - The time the MESSAGEG1 is received at process is called tr1
    - ts1 is according to parent local clock
    - tr1 is according to child local clock
      
    - Process sends another message called MESSAGE2 at ts2 to the parent
    - When parent receives the response it marks the receive time as tr2
    - ts2 is according to child local clock
    - tr2 is according to parent local clock
    
    - Offset o = (tr1 - tr2 + ts2 - ts1) / 2
    - Suppose real offset (difference between parent and child) is oreal
    - Suppose one way latency of MESSAGE1 is L1 and L2 for MESSAGE2
    - L1 and L2 are unknown
    - tr1 = ts1 + L1 + oreal ___ (1)
    - tr2 = ts2 + L2 - oreal ___ (2)
    
    - Subtracting 2 from 1
        - oreal * 2 = (tr1 - tr2) + (L2 - L1) + (ts2 - ts1)
        - oreal = 0.5 * ((tr1 - tr2) + (L2 - L1) + (ts2 - ts1))
        - oreal = o + (L2 - L1)/2
        - abs(oreal - o) < abs((L2 - L1)/2) < abs((L2 + L1)/2)
        - abs(oreal - o) < RTT (round trip time)/2 {since L2 + L1 = RTT }
    