class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val = defaultdict(int)
        for i in nums:
            val[i] += 1

        frequency = [[] for i in range(len(nums)+1)]
        for key, freq in val.items():
            frequency[freq].append(key)

        res = []
        for i in range(len(frequency)-1,0,-1):
            for num in frequency[i]:
                res.append(num)
                if len(res)>=k:
                    return res

