Multi-threaded programming
    - Each thread has its own stack, program counter, address space etc
    - Gives I/O Concurrency (advantages of using thread)
        - One program that has launched several requests and is waiting for all replies
        - Thread parallelism : Using multicore to increase throughput
        - Good for background jobs
    - Threads give a feeling of multi tasking
    - Event driven programming also helps in multi tasking (Asynchronous Programming)

- Difference between process and threads
    - A process is a container for thread
    - Threads share memory in single process
    - Process have OS assigned different memories
    
- Multi threaded challenges
    - Locking in Threads to ensure thread safe access to shared data
    - Go uses mutex to lock/unlock, and it has no idea about what is the shared object
    - Problems in threaded programming is usually solved with locks
    - Coordination in threads: Channels, sync.Cond, WaitGroup
    - Deadlock: 
        - A thread T1 waits on another thread T2 and the same thread T2 is waiting for thread T1.
        - Neither can proceed nor can release a lock
    - 