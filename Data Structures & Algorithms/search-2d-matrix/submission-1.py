class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = rows * cols - 1

        while l<=r:
            mp = l+(r-l)//2

            row = mp//cols
            col = mp%cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] <= target:
                l = mp + 1
            elif matrix[row][col] >= target:
                r = mp - 1

        return False



                

