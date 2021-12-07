class Solution(object):
    def lengthOfLastWord(self, s):
        ans = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
               ans+=1
            elif 0 < ans:
                break
        return ans
             
if __name__== "__main__":
    a = Solution()
    s = "Hello World"
    print(a.lengthOfLastWord(s))
    s = "   fly me   to   the moon  "
    print(a.lengthOfLastWord(s))
    s = "luffy is still joyboy"
    print(a.lengthOfLastWord(s))