class Solution(object):
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while(i < j):
            if not s[i].isalpha():
                i+=1
            elif not s[j].isalpha():
                j-=1
            else:
                if s[i].lower() != s[j].lower():
                    return False
                i+=1
                j-=1
        return True
if __name__ == "__main__":
    a = Solution()
    print(a.isPalindrome("A man, a plan, a canal: Panama"))
    print(a.isPalindrome("race a car"))
    print(a.isPalindrome("OP"))