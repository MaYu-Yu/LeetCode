class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
if __name__ == "__main__":
    a = Solution()
    s = ["0", "e", ".", ".1"]
    for i in s:
        print(a.isNumber(i))
        