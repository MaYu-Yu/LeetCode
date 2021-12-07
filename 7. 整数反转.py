class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: return 0
        import sys,math
        ans = 0 
        s = 1 if x>0 else -1
        x = abs(x)
    # ans > MAX_VALUE / 10 溢位
        boundry = (1<<31) -1 if x>0 else 1<<31
        while x != 0 :
            ans = ans*10 + x % 10 
            if ans > boundry: return 0
            x //= 10
        return ans * s
    
if __name__ == '__main__':
    a = Solution()
    print(a.reverse(-1215))