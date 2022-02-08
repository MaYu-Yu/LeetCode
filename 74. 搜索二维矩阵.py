class Solution(object):
    def searchMatrix(self, matrix, target):
        m, n, line = len(matrix), len(matrix[0]), 0
        for i in range(m):
            if target == matrix[i][-1]:
                return True
            if target < matrix[i][-1]:
                line =  i
                l, r = 0, n - 1
                while(l <= r):
                    mid = (l + r) // 2
                    if target == matrix[line][mid]:
                        return True
                    if target < matrix[line][mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
        return False
if __name__ == "__main__":
    a = Solution()
    matrix = [[1,3]]
    target = 3
    print(a.searchMatrix(matrix, target))    
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(a.searchMatrix(matrix, target))
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    print(a.searchMatrix(matrix, target))