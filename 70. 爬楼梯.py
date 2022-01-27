class Solution(object):
    def climbStairs(self, n):
        if n < 3: return n 
    # 到3階 = {2階走(1) + 1階走(2)} 
        t1, t2, ans = 1, 2, 0
        for _ in range(3, n + 1):
            ans = t1 + t2
            t1 = t2
            t2 = ans
        return ans
if __name__ == "__main__":
    a = Solution()
    for x in range(1, 10):
        print(a.climbStairs(x))