class Solution(object):
    def minDistance(self, word1, word2):
        row = len(word1)
        col = len(word2)
        dp = [[0 for _ in range(col+1)] for _ in range(row+1)]
        # init
        for i in range(row + 1):
            dp[i][0] = i
        for i in range(col + 1):
            dp[0][i] = i
    # add = left
    # del = up
    # replace = up left
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[row][col]
if __name__ == "__main__":
    a = Solution()
    word1 = "horse"
    word2 = "ros"
    print(a.minDistance(word1, word2))
    word1 = "intention"
    word2 = "execution"
    print(a.minDistance(word1, word2))