- Consistency Specturm two ends
    - Eventual consistency with faster reads and writes
    - Strong (sequential) consistency with slower reads and writes

- Other forms of consistency between eventual and strong
    - Eventual -> Causal -> Per key sequential -> Red Blue -> Probabilistic -> CRDTs -> Strong
    
    - Per key sequential model
        - Per key all operations have a global order
        - Maintain a per key coordinator
        - All reads and writes are serializable via this coordinator
        - Coordinator is single point of failure
    
    - CRDT (Commutative Replicated Data Type):
        - Data structures for which commutative writes gives same result
        - Commutative writes mean order of writes
        - If we have a counter object, and it gets two write instructions where write means to increment
        - Order of instruction does not matter the output is same
        - CRDTs, enable servers not worry about consistency
        - End result of any permutations of writes is the same
    
    - Red Blue Consistency
        - Operations are split into red and blue groups
        - Blue ops are commutative and can be executed in any order
        - Red ops are to be executed always sequentially
    
    - Causal Consistency
        - Reads must respect partial order based on information flow
        - It returns one of potentially many options
    
- Strong consistency
    -  Linearizability
        - Each operation by a client is visible or available in real time to all other clients
    - Sequential Consistency
        - Lamport consistency, reordering based on causality, clients being able to read their own rights
    
