class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicVal = {}
        for i, item in enumerate(strs):
            hshMap = [0]*26
            for j in item:
                val = ord(j) - ord('a')
                hshMap[val] += 1

            key = tuple(hshMap)
            if key not in dicVal:
                dicVal[key] = []
            
            dicVal[key].append(item)

        res = []
        for i in dicVal.values():
            res.append(i)
            
        return res