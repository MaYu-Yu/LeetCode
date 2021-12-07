class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x < 10: return True
        pal = 0
        y = x
        while y != 0:
            pal = pal * 10 + y % 10
            y //= 10
        return True if pal == x else False
if __name__ == '__main__':
    a = Solution()
    print(a.isPalindrome(989))
