class Solution(object):
#KMP解法
# l = -1 無前後綴
# l = 有 l - 1 個前後綴
    def prefix_table(self, size, needle):
        prefix_table = ['' for _ in range(size)]
        l = -1
        prefix_table[0] = -1
        for r in range(1, size):
            while l >= 0 and needle[l + 1] != needle[r]: 
                l = prefix_table[l]
            if needle[l + 1] == needle[r]: 
                l+=1
            prefix_table[r] = l
        return prefix_table
    def strStr(self, haystack, needle):
        needle_size = len(needle)
        if needle_size == 0: return 0
        prefix_table = self.prefix_table(needle_size, needle)
        n = -1
        for h in range(len(haystack)):
            while n >= 0 and haystack[h] != needle[n + 1]:
                n = prefix_table[n]
            if haystack[h] == needle[n + 1]:
                n+=1
            if n == needle_size - 1:
                return h - n
        return -1 
if __name__== "__main__":
    a = Solution()
    print(a.strStr("aabaabaaf", "ababcabaa"))
    print(a.strStr("aabaabaaf", "aabaaf"))
    print(a.strStr("hello", "ll"))
    print(a.strStr("aaaaa", "bba"))
    print(a.strStr("a", "a"))
    print(a.strStr("", ""))
