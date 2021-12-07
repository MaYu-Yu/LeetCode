class Solution:    
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        dp = [""]*numRows
        i = 0
        flag = False # 到達尾部變成遞減->True
        for word in s:
            dp[i]+=word
            if i == numRows-1: flag = True
            if i == 0: flag = False
            if flag: i-=1
            else: i+=1
        return "".join(dp)
if __name__ == '__main__':
    a = Solution()
    print(a.convert("PAYPALISHIRING", 3))