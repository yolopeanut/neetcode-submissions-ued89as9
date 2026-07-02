class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 2 pointer binary search approach
        l = 0
        r = len(nums)-1

        while l<=r:
            mp = l+((r-l)//2)
            print(mp)
            if nums[mp] == target:
                return mp
            elif nums[mp] < target:
                l = mp+1
            else:
                r = mp-1

        return -1

