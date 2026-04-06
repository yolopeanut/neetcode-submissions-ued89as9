class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArr = defaultdict(list)
        postfixArr = defaultdict(list)

        prefix = 1
        for i,n in enumerate(nums):
            prefixArr[i] = (prefix)
            prefix *= n

        postFix = 1
        for i in range(len(nums)-1,-1,-1):
            postfixArr[i] = postFix
            postFix *= nums[i]

        res = defaultdict(list)
        for i in range(len(nums)):
            res[i] = prefixArr[i] * postfixArr[i]


        return(list(res.values()))
            