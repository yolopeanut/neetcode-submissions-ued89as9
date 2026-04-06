class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  

        for r in range(9):
            for c in range(9):
                currCellVal = board[r][c]
                if currCellVal == '.':
                    continue

                if (currCellVal in rows[r] or 
                    currCellVal in cols[c] or 
                    currCellVal in squares[r//3,c//3]):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[r//3,c//3].add(board[r][c])
        
        print(rows)
        print(cols)
        print(squares)
        return True

            

            


    
    
