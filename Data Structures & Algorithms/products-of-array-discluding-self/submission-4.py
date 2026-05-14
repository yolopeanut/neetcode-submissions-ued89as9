class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = 1
        prefixArr = []
        for i, num in enumerate(nums):
            print(i,num)
            prefixArr.append(prefix)
            prefix *= num


        print(prefixArr)

        suffix = 1
        suffixArr = []
        for i in range(len(nums)-1, -1,-1):
            print(i,nums[i])
            suffixArr.append(suffix)
            suffix *= nums[i]

        suffixArrFlipped = suffixArr[::-1]
        for i in range(len(nums)):
            suffixArrFlipped[i] = suffixArrFlipped[i] * prefixArr[i]

        return(suffixArrFlipped)

            