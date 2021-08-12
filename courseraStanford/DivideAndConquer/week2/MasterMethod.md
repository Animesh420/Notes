Let the recurrence relation of a divide and conquer algorithm be

T(n) = a * T(n/b) + O(n^d)
Here 
a ==> The number of recursive call made at each step
b ==> The size of input array passed to each recursive call
d ==> The amount of work done outside or after all recursive calls have happened.

In order to understand it in case of merge sort:
1. We make two recurive calls with merge(arr, low, mid) and merge(arr, mid+1, high)
2. We have a merge step that merges arrays like merge(arr, low, mid, high)
This way we can see we do 2 recursive calls (a == 2) at each step 
and with half of the input size of previous step (b == 2) 
and finally combine the sorted results using O(N) operations of combining. (d == 1)

By master method:

T(n)    =  O((n^d) * log(n))                if a == b ^ d
        =  O(n ^ d)                         if a < b ^ d
        =  O(n^(log a to the base b))       if a > b ^ d
        
Example:
1. Merge sort recurrence relation
    T(n) = 2* T(n/2) + O(n), a = 2, b = 2, d = 1
    a == b ^ d, therefore T(n) = O(n * log(n))

2. Karatsuba Efficient recurrence relation
    T(n) = 3 * T(n/2) + O(n) [We take 3 products of length n/2 digits (ac, bd and (a+c).(b+d)) and take O(n) to compute sum of these products]
    a = 3, b = 2, d = 1
    a > b ^ d
    T(n) = O(n^(log 3 base 2)) = O(n^1.5849625)
    
3. Karatsub Inefficient recurrence relation
    T(n) = 4 * T(n/2) + O(n) { Here we take 4 products, ac, bd, ad, bc}
    a = 4, b = 2, d = 1
    T(n) = O(n^(log 4 base 2)) = O(n^2) same as that of conventional multiplication
    
4. Fictional example
    T(n) =  2 * T(n/2) + O(n^2) {We assume merge step of merge sort takes O(n^2) time instead of O(n), maybe we 
                                 combine both arrays and do a bubble sort}
    a = 2, b = 2, c = 2
    a < b ^ d
    so T(n) = O(n^2)