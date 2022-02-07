class Solution(object):
    def setZeroes(self, matrix):
        row, col = len(matrix), len(matrix[0])
    # let 0 to None
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    matrix[i][j] = None
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == None:
                    for x in range(row):
                        if matrix[x][j] != None:
                            matrix[x][j] = 0 
                    for x in range(col):
                        if matrix[i][x] != None:
                            matrix[i][x] = 0
    # recovery -1 to 0 
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == None: 
                    matrix[i][j] = 0
        return matrix
if __name__ == "__main__":
    a = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    print(a.setZeroes(matrix))
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    print(a.setZeroes(matrix))