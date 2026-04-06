class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        res = -1
        while l<r:
            lengthDiff = r-l
            area = min(heights[r],heights[l]) * lengthDiff
            res = max(res, area)

            if heights[l] > heights[r]:
                r-=1
            
            else:
                l+=1
        return res
