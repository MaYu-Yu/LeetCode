from debug import debug_class
DEBUG = debug_class(True)
class Solution:
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True
    # set "" 對應列
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and p[j - 1] == '*'
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j] # i - 1 是 * 多次匹配
        return dp[m][n]
if __name__== "__main__":
    a = Solution()
    s = ["aa", "aa", "cb", "adceb", "acdcb", ""]
    p = ["a", "*", "?a", "*a*b", "a*c?b", ""]
    for i in range(len(s)):
        print(a.isMatch(s[i], p[i]))