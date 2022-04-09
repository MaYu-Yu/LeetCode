class Solution(object):
    def strStr(self, haystack, needle):
        def setPerfixTable(arr):
            perfix_table = []
            l = -1 
            perfix_table.append(l)
            for i in range(1, len(arr)):
                while(l != -1 and arr[i] != arr[l + 1]):
                    l = perfix_table[l]
                if arr[i] == arr[l + 1]:
                    l += 1
                perfix_table.append(l)
            return perfix_table

        max_l = len(needle) - 1
        if max_l == -1 or max_l+1 > len(haystack): return 0
        perfix_table = setPerfixTable(needle)
        l = -1
        for i in range(len(haystack)):
            while(l != -1 and haystack[i] != needle[l + 1]):
                l = perfix_table[l]
            if haystack[i] == needle[l + 1]:
                l+=1
            if l == max_l:
                return i - max_l
        return -1
if __name__== "__main__":
    a = Solution()
    print(a.strStr("aabaabaaf", "ababcabaa"))
    print(a.strStr("aabaabaaf", "aabaaf"))
    print(a.strStr("hello", "ll"))
    print(a.strStr("aaaaa", "bba"))
    print(a.strStr("a", "a"))
    print(a.strStr("", ""))
