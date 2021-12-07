class Solution(object):
    def generateMatrix(self, n):
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        l, r, t, b = 0, n - 1, 0, n - 1
        num = 1
        while True:
        # right
            for j in range(l, r + 1):
                matrix[t][j] = num
                num+=1
            t+=1
            if t > b: break
        # down
            for i in range(t, b + 1):
                matrix[i][r] = num
                num+=1
            r-=1
        # left
            for j in range(r, l - 1, -1):
                matrix[b][j] = num
                num+=1
            b-=1
        # up
            for i in range(b, t - 1, -1):
                matrix[i][l] = num
                num+=1
            l+=1
        return matrix
if __name__== "__main__":
    a = Solution()
    n = [i for i in range(1, 21)]
    for i in n:
        print(a.generateMatrix(i))