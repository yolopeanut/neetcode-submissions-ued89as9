class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort input array
        nums.sort()
        res = []

        #target is 0    
        for i,n in enumerate(nums):
            if n >0:
                break

            if i>0 and n == nums[i-1]:
                continue

            # the 2nd target should equals these 2
            target2 = 0 - n

            lptr = i+1
            rptr = len(nums) - 1

            print(nums, target2)

            while lptr<rptr:
                sumNum = nums[rptr] + nums[lptr]

                # if diff<target2, then left inc
                if sumNum < target2:
                    lptr +=1

                # if diff>target2, then right dec
                elif sumNum > target2:
                    rptr -=1

                else:
                    # if target2 found, add to res
                    res.append([nums[i],nums[lptr],nums[rptr]])
                    lptr +=1
                    rptr -=1
                    while nums[lptr] == nums[lptr-1] and lptr<rptr:
                        lptr+=1

        return(res)

