class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}

        for i, num in enumerate(nums):
            complement = target-num

            if complement in numsDict:
                return [numsDict[complement],i]
            
            numsDict[num] = i


# nums[0] == target - nums[i]