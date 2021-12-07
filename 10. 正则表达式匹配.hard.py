class Solution(object):
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
    # 初始化
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 2]
                    else:
                        dp[i][j] = dp[i][j - 2]
        return dp
if __name__ == '__main__':
    a = Solution()
    #print(a.isMatch("aa","a"))
    x = a.isMatch("aaa","ab*a*c*a")
    for i in x:
        for j in i:
            print(j, end=' ')
        print()
