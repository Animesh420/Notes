- S is a time server, universally well known time source, which replies its time
- All processes P synchronize with time server S
    - Process P asks time server S what is the time
    - By the time process P gets the reading from S it updates its time with what S says
    - This way of measuring time is incorrect as by the time P receives response from S, time has moved
    on, as processes communicate with non-zero delay
      

- Cristian's Algorithm
    - P measures the round trip time called RTT of message exchange (denoted by RTT)
    - P has heuristic or measure information about the time taken for going P -> S (let this be min1)
    - P has also the heuristic or measure information about the time taken for going S -> P (let this be min2)
    - min1 and min2 depend on things like operation system overhead to buffer messages, TCP time to queue messages etc
    - This way the actual time at P when it receives response is between [t + min2, t + RTT - min1]
    - t + min2: This would be the case where the response message from S -> P took exactly min2 time units
    - t + RTT - min1: This occurs when the query message took exactly min1 seconds to reach S from P.
    - In practice the accepted time is average of two i.e. t + (RTT + min2 - min1) / 2
    - So error is bounded by (RTT + min2 - min1)/2 -> Error depends on RTT
    
    - EDGE CASES
        - If S replies with a time that is less than the time at P, you take the time at P, (never go back)
        - If the S replies time that is always ahead of the measured time at P, then you may consider increasing the speed of P
        - If error is too high, take multiple readings and average them
    
    
    