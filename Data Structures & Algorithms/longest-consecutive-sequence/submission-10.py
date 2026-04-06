class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for i,n in enumerate(numSet):
            if n-1 in numSet: continue

            currVal = n
            currLen = 1

            while (currVal + 1) in numSet:
                currVal +=1
                currLen +=1

            res = max(res,currLen)

        return(res)

            
        



             