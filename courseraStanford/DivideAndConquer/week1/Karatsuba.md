1. Product of two n-digit numbers x and y 
Inefficient approach:
1. Compute partial product for each digit in y with x
2. For each partial product shift by 10 ^ (location of digit in y, starting from 0)
3. Add all the shifted parital products and get the result
Number of operations:
1. 2n for each partial product ( n for  multiply and n for carry addition)
2. This is upper bound
3. Now to have full product we need to have 2n * n i.e. O(n^2) algorithm , quadratic in input number of digits
where n is the number of digits in a number.

Karatsuba Algorithm:
Let x = (10^(n/2)) * a + b and y = (10^(n/2)) * c + d, where n is the total number of digits 
x * y = (10^n) * (ac) + (10^(n/2)) (ad + bc) + bd
Computing these four products ac, bd, ad and bc we can get the product of x and y.
A thing to observe, ad + bc = (a + b) * (c + d) - ac - bd, so we can compute only three products to find the x * y value.
Base case of this algorithm is when n = 1 and we get a single digit, we multiply that in a single operation and return
