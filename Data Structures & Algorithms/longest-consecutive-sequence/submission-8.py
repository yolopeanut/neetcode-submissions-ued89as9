class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        print(numSet)
        res = 1

        if len(nums) <= 1:
            return len(nums)

        for i,n in enumerate(numSet):
            currVal = n
            currLen = 1

            while (currVal + 1) in numSet:
                currVal +=1
                currLen +=1
                res = max(res,currLen)

        return(res)

            
        



             