class Solution(object):
    def solveSudoku(self, board):
        def setBoard(board, space, rows, columns, boxes, index):
            global Flag
            if index == len(space):
                Flag = True
                return

            i, j = space[index]
            for val in range(9):
                if not rows[i][val] and not columns[j][val] and not boxes[i//3][j//3][val]:
                # set
                    rows[i][val] = True
                    columns[j][val] = True
                    boxes[i//3][j//3][val] = True
                    board[i][j] = str(val + 1)
                    setBoard(board, space, rows, columns, boxes, index + 1)
                # remove
                    rows[i][val] = False
                    columns[j][val] = False
                    boxes[i//3][j//3][val] = False
                if Flag: return 
        global Flag 
        Flag = False
        rows = [[False for _ in range(9)] for _ in range(9)]
        columns = [[False for _ in range(9)] for _ in range(9)]
        boxes = [[[False for _ in range(9)] for _ in range(3)] for _ in range(3)]
        space = list()
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    space.append([i,j])
                else:
                    val = int(board[i][j]) - 1
                    rows[i][val] = True
                    columns[j][val] = True
                    boxes[i//3][j//3][val] = True
        setBoard(board, space, rows, columns, boxes, 0)  
        return board
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
    print(a.solveSudoku(board))