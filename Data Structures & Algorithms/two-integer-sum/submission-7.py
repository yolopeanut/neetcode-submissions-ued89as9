class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i in range(len(nums)):
            print(numDict)
            complement = target - nums[i]
            
            if complement in numDict:
                return [numDict[complement], i]
            
            numDict[nums[i]] = i
        
        