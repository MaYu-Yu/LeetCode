class Solution(object):
    def myPow(self, x, n):
        def pow2(x, n):
            if n == 0: return 1.0
            y = pow2(x, n // 2)
            return y * y if n % 2 == 0 else y * y * x 
        return pow2(x, n) if n >= 0 else 1.0 / pow2(x, -n)
if __name__== "__main__":
    a = Solution()
    x = 2.00000
    n = 10
    print(a.myPow(x, n))
    x = 2.10000
    n = 3
    print(a.myPow(x, n))
    x = 2.00000
    n = -2
    print(a.myPow(x, n))
    n = pow(2, 31) - 1
    x = 99.9
    print(a.myPow(x, n))