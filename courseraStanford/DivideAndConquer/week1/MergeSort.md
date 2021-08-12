Merge sort:
1. Recursively divides the array and merges them back
2. code at mergeSortExample.py
3. At every level j, there are 2^j arrays each of size n/(2^j) and there are log(n) levels
so total time complexity is (n/(2^j) * (2^j)) * log(n) = n log(n)