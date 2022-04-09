class Solution(object):
    def hanota(self, A, B, C):
        def moveXtoY(x, y):
            y.append(x[-1])
            x.pop()
        def solve(n, a, b, c):
            if n == 1:
                moveXtoY(a, c)
            else:
                solve(n - 1, a, c, b)
                solve(1    , a, b, c)
                solve(n - 1, b, a, c)
        solve(len(A), A, B, C)
if __name__ == "__main__":
    x = Solution()
    a = [2, 1, 0]
    b = []
    c = []
    x.hanota(a,b,c)
    a = [1, 0]
    b = []
    c = []    
    x.hanota(a,b,c)