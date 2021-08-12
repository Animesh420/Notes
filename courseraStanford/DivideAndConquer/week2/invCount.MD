## The inversion count problem
The inversion count problem in an array of size n is to count
all the pairs i, j where 0 <= i < n and 0 <= j < n such that
i < j and A[i] > A[j]

Approach:
For the array there are three types of pairs of i, j that contribute to inversion count
a) i, j <= n/2 --> we call this left inversion
b) i, j > n/2 --> we call this right inversion
c) i <= n/2 <= j --> we call this split inversion

We can derive a divide and conquer approach to the problem
using the fact that 
1. At base case when n == 1: there is no inversion possible
so return 0
2. for the other cases return the sum of a), b) and c).

This counts the inversions