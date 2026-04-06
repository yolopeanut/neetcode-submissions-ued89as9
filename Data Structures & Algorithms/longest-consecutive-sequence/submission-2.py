class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # Sequence starter
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length +=1

                if length>longest:
                    longest = length

            # Middle of sequence 

        return longest



             