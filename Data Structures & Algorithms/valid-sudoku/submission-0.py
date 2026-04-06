class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                currentCell = board[r][c]
                if currentCell ==".":
                    continue
                
                if (currentCell in rows[r] or currentCell in cols[c] or currentCell in squares[(r//3,c//3)]):
                    return False
                
                cols[c].add(currentCell)
                rows[r].add(currentCell)
                squares[(r//3,c//3)].add(currentCell)

        print(rows,cols)
        return True

