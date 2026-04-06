class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i in range(len(nums)):
            prevMap[nums[i]] = i

        for i in range(len(nums)):
            compliment = target - nums[i]
            print(compliment)

            if compliment in prevMap and i != (prevMap[compliment]):
                return [i,prevMap[compliment]]




