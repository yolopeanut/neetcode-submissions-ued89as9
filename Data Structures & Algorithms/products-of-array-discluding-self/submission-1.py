class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArr = [[1] for i in nums]
        postfixArr = [[1] for i in nums]

        prefix = 1
        for i,n in enumerate(nums):
            prefixArr[i] = prefix
            prefix *= n

        postFix = 1
        for i in range(len(nums)-1,-1,-1):
            postfixArr[i] = postFix
            postFix *= nums[i]

        print(prefixArr,postfixArr)

        res = [prefixArr[i] * postfixArr[i] for i in range(len(nums)) ]
        return (res)

