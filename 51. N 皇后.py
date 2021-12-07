from debug import debug_class
DEBUG = debug_class(True)
class Solution(object):
    def solveNQueens(self, n):   
        def isVaild(n, map, x, y):
            if x == 0: return True
        # 上方
            for i in range(0, x):
                if map[i][y] == 'Q': 
                    return False
        # 左上
            i, j = x - 1, y - 1
            while i >= 0 and j >= 0:
                if map[i][j] == 'Q': 
                    return False
                i-=1
                j-=1
        # 右上
            i, j = x - 1, y + 1
            while i >= 0 and j < n:
                if map[i][j] == 'Q': 
                    return False
                i-=1
                j+=1
            return True
        def fill(n, ans, map, i):
            if i == n: 
                ans.append(map[:])
                return 
            for j in range(n):
                if isVaild(n, map, i, j):
                    map.append('.' * j + 'Q' + '.' * (n - j - 1))
                    fill(n, ans, map, i + 1)
                    map.pop()
        ans = list()
        fill(n, ans, [], 0)
        return ans
if __name__== "__main__":
    a = Solution()
    for i in range(10):
        print("----------"+str(i)+"----------")
        print(a.solveNQueens(i))