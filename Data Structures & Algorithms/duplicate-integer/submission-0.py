class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        defaultVal = False
        uniqueSet = set(nums)
        for num in uniqueSet:
            if nums.count(num) > 1:
                return True

        return defaultVal

            
         