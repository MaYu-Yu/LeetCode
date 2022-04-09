class Solution(object):
    def totalNQueens(self, n):   
        def isVaild(n, map, x, y):
            if x == 0: return True
        # 上方
            for i in range(0, x):
                if map[i][y]: 
                    return False
        # 左上
            i, j = x - 1, y - 1
            while i >= 0 and j >= 0:
                if map[i][j]: 
                    return False
                i-=1
                j-=1
        # 右上
            i, j = x - 1, y + 1
            while i >= 0 and j < n:
                if map[i][j]: 
                    return False
                i-=1
                j+=1
            return True
        def fill(n, map, i):
            if i == n: 
                global ans
                ans+=1
                return
            for j in range(n):
                if isVaild(n, map, i, j):
                    map[i][j] = True
                    fill(n, map, i + 1)
                    map[i][j] = False
        map = [[False for _ in range(n)] for _ in range(n)]
        global ans 
        ans = 0
        fill(n, map, 0)
        return ans
if __name__== "__main__":
    a = Solution()
    for i in range(1,5):
        print("----------"+str(i)+"----------")
        print(a.totalNQueens(i))