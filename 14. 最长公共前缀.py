class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if strs == []: return ''
        mod = strs[0]
        size = len(mod)
        ans = ""
        try: 
            for i in range(size):
                for curr_char in strs:
                    if curr_char[i] != mod[i]: return ans
                ans += mod[i]
        except IndexError:
            return ans
        return ans
if __name__ == '__main__':
    a = Solution()
    testList = ['','b']
    print(a.longestCommonPrefix(testList))
        