from debug import debug_class
DEBUG = debug_class(True)
class Solution(object):
    def rotate(self, matrix):
        def printm(matrix):
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    print(matrix[i][j], end = ', ')
                print()
            print("----------------------------")
        max_i, max_j = len(matrix) - 1, len(matrix[0]) - 1
    # 翻轉 list
        for i in range(max_i + 1):
            for j in range((max_j + 1) // 2):
                matrix[i][j], matrix[i][max_j - j] = matrix[i][max_j - j], matrix[i][j]
    # 對角交換
        for i in range(max_i):
            for j in range(max_j - i):
                #print("swap([{}, {}], [{}, {}])".format(i,j, max_i - j, max_j - i))
                matrix[i][j], matrix[max_i - j][max_j - i] = matrix[max_i - j][max_j - i], matrix[i][j]
        return matrix
if __name__== "__main__":
    a = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(a.rotate(matrix))
    print(a.rotate(matrix))
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    print(a.rotate(matrix))    
    # matrix = [[1]]
    # print(a.rotate(matrix))    
    # matrix = [[1,2],[3,4]]
    # print(a.rotate(matrix))        