class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            lCnt = [0]*26
            for letter in s:
                lCnt[ord(letter) - ord('a')] += 1
            
            key = tuple(lCnt)

            res[key].append(s)
        
        return list(res.values())