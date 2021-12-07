class Solution:
    def romanToInt(self, s: str) -> int:
        size = len(s)
        val = { 'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        i = size-1
        ans = val[s[i]]
        while i > 0:
            if val[s[i-1]] < val[s[i]]: ans-=val[s[i-1]] 
            else: ans+=val[s[i-1]]
            i-=1
        return ans

if __name__ == '__main__':
    a = Solution()
    print(a.romanToInt("MCMXCIV"))
        