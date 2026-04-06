class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        itemSet = set()

        for num in nums:
            
            itemSet.add(num)
        
        if len(itemSet) == len(nums):
            return False

        return True 