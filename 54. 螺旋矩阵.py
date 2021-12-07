class Solution(object):
    def spiralOrder(self, matrix):
        ans = []
        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        
        while True:
        # right
            for j in range(l, r + 1):
                ans.append(matrix[t][j])
            t+=1
            if t > b: break
        # down
            for i in range(t, b + 1):
                ans.append(matrix[i][r])
            r-=1
            if r < l: break
        # left
            for j in range(r, l - 1, -1):
                ans.append(matrix[b][j])
            b-=1
            if b < t: break
        # up
            for i in range(b, t - 1, -1):
                ans.append(matrix[i][l])
            l+=1
            if l > r: break
        return ans
if __name__== "__main__":
    a = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(a.spiralOrder(matrix))
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(a.spiralOrder(matrix))
    matrix = [[1]]
    print(a.spiralOrder(matrix))    
