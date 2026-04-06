class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        winSize = k
        resA = []

        currWin = [0,0]
        currMaxInWind = float("-inf")
        
        l = 0

        # Get first window max
        for i in range(k):
            currMaxInWind = max(currMaxInWind,nums[i])

        # resA.append(currMaxInWind)

        # print(currMaxInWind)

        for r in range(winSize,len(nums)+1):

            print(l,r,nums[l:r])

            # Check max of new number
            currMaxInWind = max(currMaxInWind,nums[r-1])
            resA.append(currMaxInWind)
            print(currMaxInWind)

            # check l if its the same as max, if it is, recalculate for whole thing.
            if nums[l] == currMaxInWind and r+1<len(nums)+1:
                print(True)
                currMaxInWind = float("-inf")
                print(nums[l+1:r+1])
                for i in nums[l+1:r+1]:
                    currMaxInWind = max(currMaxInWind,i)


            l+=1
        # print(resA)
        return(resA)