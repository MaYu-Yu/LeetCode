class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 特判
        size = len(s)
        if size < 2:
            return s
        # 得到预处理字符串
        t = "#"
        for i in range(size):
            t += s[i]
            t += "#"
        # 新字符串的长度
        t_len = 2 * size + 1
        # 当前遍历的中心最大扩散步数，其值等于原始字符串的最长回文子串的长度
        max_len = 1
        # 原始字符串的最长回文子串的起始位置，与 max_len 必须同时更新
        start = 0

        for i in range(t_len):
            cur_len = self.center_spread(t, i)
            if cur_len > max_len:
                max_len = cur_len
                start = (i - max_len) // 2
        return s[start: start + max_len]

    def center_spread(self, s, center):
        size = len(s)
        i = center - 1
        j = center + 1
        step = 0
        while i >= 0 and j < size and s[i] == s[j]:
            i -= 1
            j += 1
            step += 1
        return step


if __name__ == '__main__':
    a = Solution()
    word = "banana"
    print(a.longestPalindrome(word))
