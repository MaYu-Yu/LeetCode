class Solution(object):
    def minPathSum(self, grid):
        def setDp(dp, m, n):
            for i in range(1, n): dp[0][i] += dp[0][i - 1]
            for i in range(1, m): dp[i][0] += dp[i - 1][0]
            for i in range(1, m):
                for j in range(1, n):
                    dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
            return dp[m - 1][n - 1]              
        m = len(grid)
        n = len(grid[0])
        return setDp(grid, m, n)
if __name__ == "__main__":
    a = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(a.minPathSum(grid))
    grid = [[1,2,3],[4,5,6]]
    print(a.minPathSum(grid))    