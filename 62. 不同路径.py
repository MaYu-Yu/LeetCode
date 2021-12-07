class Solution(object):
    def uniquePaths(self, m, n):
        def factorial(x):
            if x > 1:
                return x * factorial(x-1) 
            return 1
        m-=1
        n-=1
        return factorial(m+n) // factorial(m) // factorial(n)
if __name__== "__main__":
    a = Solution()
    m, n = 3, 7
    print(a.uniquePaths(m, n))
    m, n = 3, 2
    print(a.uniquePaths(m, n))
    m, n = 7, 3
    print(a.uniquePaths(m, n))