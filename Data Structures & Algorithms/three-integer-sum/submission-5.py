class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # value = target - (value + value)
        nums.sort()
        print("sorted:",nums) #O(N)
        threeSumPairs = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            firstVal = nums[i]
            conjugate = 0 - nums[i]
            print("conjugate:",conjugate)

            leftPtr = i+1
            rightPtr = len(nums) -1
            while leftPtr < rightPtr:
                threeS = nums[i] + nums[leftPtr] + nums[rightPtr]
                if threeS >0:
                    rightPtr -=1
                elif threeS <0:
                    leftPtr +=1
                
                else:
                    threeSumPairs.append([nums[i],nums[leftPtr],nums[rightPtr]])
                    leftPtr+=1
                    rightPtr-=1

                    while nums[leftPtr] == nums[leftPtr - 1] and leftPtr < rightPtr:
                        leftPtr += 1

        return threeSumPairs


