class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        for i,num in enumerate(nums):
            res[num] += 1

        print(res.values())
        sorted_desc = sorted(res.items(), key=lambda item: item[1], reverse=True)
        top_k = [item[0] for item in sorted_desc[:k]]
        return top_k
    