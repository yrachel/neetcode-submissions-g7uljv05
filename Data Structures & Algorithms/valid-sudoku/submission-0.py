import numpy as np
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        column = {}
        square = {}

        return self.allValid(0, 0, row, column, square, np.array(board))
    
    def allValid(self, r, c, row, column, square, board):
        if r > board.shape[0] - 1 or c > board.shape[0] - 1:
            return True

        sq = ((r//3) * 3, (c // 3) * 3)
        
        if r not in row:
            row[r] = self.isValid(board[r])
        if c not in column:
            column[c] = self.isValid(board[:,c])
        if sq not in square:
            square[sq] = self.isValidSquare(board, sq)
        return row[r] and column[c] and square[sq] and self.allValid(r + 1, c, row, column, square, board) and self.allValid(r, c + 1, row, column, square, board)

    def isValid(self, row):
        seen = set()

        for r in row:
            if r != ".":
                if r in seen:
                    return False
                else:
                    seen.add(r)
        return True
    
    def isValidSquare(self, board, sq):
        seen = set()
        r, c = sq

        for i in range(r, r+3):
            for j in range(c, c+3):
                curr = board[i][j]

                if curr != ".":
                    if curr in seen:
                        return False
                    else:
                        seen.add(curr)
        return True