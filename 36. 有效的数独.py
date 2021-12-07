class Solution:
    def isValidSudoku(self, board):
        rows = [[False for _ in range(9)] for _ in range(9)]
        columns = [[False for _ in range(9)] for _ in range(9)]
        boxes = [[[False for _ in range(9)] for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num) - 1
                    if rows[i][num]: 
                        return False
                    else: 
                        rows[i][num] = True

                    if columns[j][num]:
                        return False
                    else:
                        columns[j][num] = True
                    
                    if boxes[i//3][j//3][num]:
                        return False
                    else:
                        boxes[i//3][j//3][num] = True
        return True
if __name__== "__main__":
    a = Solution()
    board = [
        ["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"] ]
    print(a.isValidSudoku(board))
    board = [
        ["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"] ]
    print(a.isValidSudoku(board))