class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsDict = defaultdict(set)
        longest = 0

        for n in nums:
            # Finding starting sequences
            if (n-1) not in nums:
                lengthSeq = 0
                while (n+lengthSeq) in nums:
                    lengthSeq += 1
                
                longest = max(longest,lengthSeq)
        
        return (longest)

