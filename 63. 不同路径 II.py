class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        def setDp(obstacleGrid, dp, m, n):
            for d in range(1, m):
                for r in range(1, n):
                    if obstacleGrid[d][r] == 1: continue
                    dp[d][r] = dp[d - 1][r] + dp[d][r - 1] 
            print(dp)
            return dp[m - 1][n - 1]
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
    # init dp
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m): 
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for i in range(n): 
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1
        return setDp(obstacleGrid, dp, m, n)
if __name__ == "__main__":
    a = Solution()
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    print(a.uniquePathsWithObstacles(obstacleGrid))
    obstacleGrid = [[0,1],[0,0]]
    print(a.uniquePathsWithObstacles(obstacleGrid))
    obstacleGrid = [[1]]
    print(a.uniquePathsWithObstacles(obstacleGrid))
    obstacleGrid = [[0,0,0,0,1,0,0],[0,0,0,0,0,0,0],[0,1,0,0,1,0,0]]
    print(a.uniquePathsWithObstacles(obstacleGrid))
    
