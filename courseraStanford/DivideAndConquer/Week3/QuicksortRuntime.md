# Quicksort runtime analysis
1. The runtime of quick sort is dominated by comparison operation that means for each choice of pivot we have a 
certain number of comparisons happening that dominate the performance of quick sort

2. Let C(s) denote the total number of comparisons for a random choice "s" of pivot.
3. We shall show E[C(s)] = O(nlogn) and that will measure the time complexity of quick sort.
4. For this let us define two variables:
    a. Z(i) --> This denotes the ith smallest element in the array
    b. X(ij) --> This denotes the probability that Z(i) is compared with Z(j)

5. We can see X(ij) is a bernoulli random variable as it takes value only 0 or 1.
    X(ij) = 0 --> This means that the two array positions (i) and (j) are never compared
    This can happen when the position i is in different sub array as compared to position (j)
    This can also happen when none of i or j is a pivot and therefore they dont get compared.
    Reminder: In quick sort, the pivot element is compared to each element of the subarray always.
    
    X(ij) = 1 --> This can only happen if either of Z(i) is a pivot or Z(j) is a pivot.
    In that case only Z(i) will be compared against Z(j)
    
6. We can express C(s) with the following lines of code.
    n = len(arr)
    for i in range(1, n-1):
        for j in range(i+1, n):
            E[X(ij)]
 
    Here we say that the total comparison C(s) can be expressed as summation of comparisons over all indices i, j 
    such that i < j. It is intuitive to see that if positions i and j are compared against each other we take the sum 
    of all such possibilities as sum of E(X(ij))

7. Now X(ij) is a Bernouli random variable and the E(Bernouli Random variable) = p
   Where p - Probability that Bernouli random variable is 1
   
8 The probability that the random variable X(ij) = 1 is only possible if i or j are chosen as pivot from a set of elements
from i to j .
Probability of choosing i as pivot from elements between i to j (both inclusive) = (j - i + 1) ^ -1
Probability of choosing j as pivot from elements between i to j (both inclusive) = (j - i + 1) ^ -1
Therefore total probability = 2/(j- i + 1)

9 Now our code becomes
n = len(arr)
for i in range(1, n-1)
    for j in range(i+1, n):
    2/(j-i+1)
    
This is actually two summations outer one depends on i and the inner one depends on j

10 . If we evaluate the inner summation starting at j = i + 1
we get an infinite series as (1/2) + (1/3) + (1/4) ....
We see that this series is upper bounded by function f(x) = 1/x

11. Since this is sum of discrete values, we can integrate and replace it with an upper bound
and integration of 1/x is log(x), applying limits we get log(n)

12. Outer loop evaluates to a constant "n" since the inner loop is a constant and does not depend on "i" the outer loop 
is a simple summation of numbers from 1 to n - 1.

13 therefore the E(C(s)) = 2 * n (# from the outer loop) * log(n) (# from the inner loop)
Upper bounded by O(nLog(n))
    

