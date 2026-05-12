class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        passed = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            print(complement)
            if complement in passed:
                print("Found")
                return [passed[complement],i]

            passed[nums[i]] = i

        print(passed)

        