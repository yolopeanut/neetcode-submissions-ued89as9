class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDictCount = defaultdict(int)
        freqBucket = [[] for num in nums]

        for i in nums:
            numsDictCount[i] +=1
        
        for i,n in numsDictCount.items():
            freqBucket[n-1].append(i)

        res = []
        for i in range(len(freqBucket)-1,-1,-1):
            for num in freqBucket[i]:
                res.append(num)

                if len(res)>=k:
                    return res
