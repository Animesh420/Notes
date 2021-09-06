- Key Value store:
    - Map a key to a given value
    - Example:  
        1. tweet id -> information about tweet 
        2. amazon item number -> information about it
        3. Flight number -> information about flight
        4. bank account -> Account information
    - Need to maintain this data in a distributed hash table

    - Properties of modern workloads
        - data is large and unstructured
        - Lots of random reads and writes
        - Sometimes write heavy
        - Foreign keys rarely used
        - joins are infrequent
        
    - Needs of modern workloads
        - Speed
        - Avoid single point of failure
        - Lower total cost of operation
        - Fewer system admins
        - Incremental scalability
        - Scale out (horizontal scaling), rather than scale up  (vertical scaling)
    
    - NoSQL
        - Not Only SQL
        - APIs supported, get(key), put(key, value)
        - CQL -> Cassandra Query Language
        - Tables : {"Column Families" : "Cassandra", "Table": "HBase", "Collection": MongoDB}
        - Tables may be unstructured, and they don't have schema, some item/column may be missing
        - Don't support join or foreign keys
        - Can have index tables
        - Use column oriented storage
            - RDBMS stores rows together, keys and other information are stored together in a disk
            - NoSQL stores a column together or a group of columns
            - Entries within a column are indexed and easy to locate given a key
            - Range searches in a column are fast since you don't need to fetch the entire database
            - Examples: Getting all blog ids that where updated within the past month
                - In RDBMS, entire table is searched, filtered and corresponding blog id columns are returned
                - In NoSql database, search is reduced to column that has blog id, so search space is small and results 
                are returned faster
            
    