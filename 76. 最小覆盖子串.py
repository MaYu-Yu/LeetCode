class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
if __name__== "__main__":
    a = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(a.minWindow(s, t))
    s = "a"
    t = "a"
    print(a.minWindow(s, t))
    s = "a"
    t = "aa"
    print(a.minWindow(s, t))