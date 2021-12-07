class Solution:
    def intToRoman(self, num: int) -> str:
        val = { 'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
        ans = ''
        
        for i in val:
            while num - val[i] >= 0: 
                ans+=i
                num-=val[i]
        return ans

if __name__ == '__main__':
    a = Solution()
    print(a.intToRoman(3))
        