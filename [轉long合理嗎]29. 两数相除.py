class Solution(object):
    # A B useAdd isMinus
    # + +   F     F   +
    # + -   T     T   +
    # - +   T     T   +
    # - -   F     F   +
    def divide(self, dividend, divisor):
        import math
        if divisor == 0: return 0
        if (dividend == math.pow(-2, 31) and divisor == -1): return int(math.pow(2, 31) - 1)
        if (dividend == math.pow(2, 31) and divisor == 1): return int(math.pow(2, 31) - 1)
        max = math.pow(2, 23) - 1 
        min = math.pow(-2, 23)
        isMinus = (dividend > 0) ^ (divisor > 0)
        if (dividend < 0): dividend = -dividend
        if (divisor < 0): divisor = - divisor
        quo = 0 
        while dividend >= divisor:
            dividend -= divisor
            quo+=1
        return -quo if isMinus else quo

if __name__== "__main__":
    a = Solution()
    print(a.divide(10, 3))
    print(a.divide(7, -3))
    print(a.divide(-1, 1))