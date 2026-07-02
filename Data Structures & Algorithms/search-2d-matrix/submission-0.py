class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        targetRowIdx = 0
        for i in range(len(matrix)):
            l = matrix[i][0]
            r = matrix[i][len(matrix[i])-1]

            if target == r:
                return True
            
            # Go next loop
            elif target>r:
                continue
            
            # store and break
            elif target<r:
                targetRowIdx = i
                break
        
        targetRow = matrix[targetRowIdx]
        l = 0
        r = len(targetRow)-1
        print(targetRow, l,r)
        while l<=r:
            mp = l+(r-l)//2

            if targetRow[mp]==target:
                return True
            
            elif targetRow[mp]<target:
                l = mp+1
            elif targetRow[mp]>target:
                r = mp-1

        return False


                

