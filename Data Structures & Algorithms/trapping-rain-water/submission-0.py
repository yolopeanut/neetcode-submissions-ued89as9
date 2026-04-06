class Solution:
    def trap(self, height: List[int]) -> int:
        # res = 0
        # maxLHeight = 0
        # maxRHeight = 0
        # for i, e in enumerate(height):
        #     water = maxLHeight - e
        #     if water>0:
        #         res += water
        #         print(i, water, res)
            
            

        #     maxLHeight = max(e, maxLHeight)

        # print(res)

        if not height:
            return 0


        l,r = 0, len(height)-1
        maxLHeight = height[l]
        maxRHeight = height[r]
        res = 0

        while l<r:
            if maxLHeight<maxRHeight:
                l += 1
                maxLHeight = max(maxLHeight, height[l])
                res += maxLHeight - height[l]
            else:
                r -= 1
                maxRHeight = max(maxRHeight, height[r])
                res += maxRHeight-height[r]
        return res