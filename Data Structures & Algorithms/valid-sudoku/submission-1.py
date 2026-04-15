
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        column = defaultdict(set)
        square = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                curr = board[i][j]
                if curr != ".":
                    if curr in row[i] or curr in column[j] or curr in square[i // 3, j // 3]:
                        return False
                    else:
                        row[i].add(curr)
                        column[j].add(curr)
                        square[(i // 3, j // 3)].add(curr)

        return True