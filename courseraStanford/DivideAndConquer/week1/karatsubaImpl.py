class Solution:

    def karatsuba(self, x, y, n):
        if n == 1:
            return x * y

        divisor = pow(10, n // 2)
        a, b = divmod(x, divisor)
        c, d = divmod(y, divisor)

        p1 = self.karatsuba(a, c, n // 2)
        p2 = self.karatsuba(b, d, n // 2)
        p3 = self.karatsuba((a + b), (c + d), n // 2)
        mid = p3 - p2 - p1
        return p1 * divisor * divisor + mid * divisor + p2


if __name__ == '__main__':
    so = Solution()
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627
    n = 64
    out = so.karatsuba(x, y, n)
    print(out)
