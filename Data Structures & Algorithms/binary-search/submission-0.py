class Solution:
    def search(self, nums: List[int], target: int) -> int:
        indx = 0
        for i in nums:
            if i == target:
                return indx
            else:
                indx +=1

        return -1