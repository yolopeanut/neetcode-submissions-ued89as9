class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        threeSumPairs = []
        
        for i in range(len(nums)-2):  # we need at least 3 numbers remaining
            # Skip duplicates for first number
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            firstVal = nums[i]
            conjugate = 0 - firstVal
            
            leftPtr = i + 1
            rightPtr = len(nums) - 1
            
            while leftPtr < rightPtr:
                currentSum = nums[leftPtr] + nums[rightPtr]
                
                if currentSum == conjugate:
                    threeSumPairs.append([firstVal, nums[leftPtr], nums[rightPtr]])
                    
                    # Skip duplicates for leftPtr
                    while leftPtr < rightPtr and nums[leftPtr] == nums[leftPtr + 1]:
                        leftPtr += 1
                    # Skip duplicates for rightPtr
                    while leftPtr < rightPtr and nums[rightPtr] == nums[rightPtr - 1]:
                        rightPtr -= 1
                        
                    leftPtr += 1
                    rightPtr -= 1
                    
                elif currentSum < conjugate:
                    leftPtr += 1
                else:  # currentSum > conjugate
                    rightPtr -= 1
                    
        return threeSumPairs


