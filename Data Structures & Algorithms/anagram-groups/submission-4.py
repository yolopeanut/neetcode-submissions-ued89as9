class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicVal = defaultdict(list)
        for i, item in enumerate(strs):
            hshMap = [0]*26
            for j in item:
                hshMap[ord(j) - ord('a')] += 1

            key = tuple(hshMap)
            dicVal[key].append(item)

        return list(dicVal.values())