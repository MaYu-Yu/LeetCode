class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
    # l為目前已判斷長度，i為首字，j為目前判斷點
        for l in range(n):
            for i in range(n):
                j = i + l
                if j >= n:
                    break
            # 將首字SET True
                if l == 0:
                    dp[i][j] = True
            # 判斷相同字(隔壁)
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
            # 判斷相同字(跨j格)
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
            # 此次長度超過當前長度就update
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j+1]
        return ans

if __name__ == '__main__':
    a = Solution()
    word = "aa"
    print(a.longestPalindrome(word))
