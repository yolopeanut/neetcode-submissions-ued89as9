class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        resTmp = defaultdict(int)
        for i in nums:
            resTmp[i] += 1
        print(resTmp)

        freqArr = [[] for i in range(len(nums))]
        print(freqArr)
        for key,val in resTmp.items():
            freqArr[val-1].append(key)
        print(resTmp,freqArr)


        res =[]
        for i in range(len(freqArr)-1, -1, -1):
            for item in freqArr[i]:
                res.append(item)

                if len(res) == k:
                    return res

            


