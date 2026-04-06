class Solution:
    def trap(self, height: List[int]) -> int:
        # l,r = 0,len(height)-1

        # maxL = height[l]
        # maxR = height[r]
        # res = 0

        # while l<r:

        #     if maxL<maxR:
        #         l += 1
        #         maxL = max(height[l], maxL)
        #         res += (maxL - height[l])

        #     else:
        #         r -= 1
        #         maxR = max(height[r], maxR)
        #         res += (maxR - height[r])

        # return(res)

        n = len(height)
        prefixArr = [0] * n
        postfixArr = [0] * n

        prefixArr[0] = height[0]
        for i in range(1, n):
            prefixArr[i] = max(prefixArr[i-1], height[i])

        postfixArr[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            postfixArr[i] = max(postfixArr[i+1], height[i])

        print(prefixArr)
        print(postfixArr)

        res = 0
        for i in range(n):
            res += min(prefixArr[i],postfixArr[i]) - height[i]
            print(prefixArr[i],postfixArr[i], height[i], res)

        return res





