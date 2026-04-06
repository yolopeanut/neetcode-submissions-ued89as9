class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            letterCnt = [0] * 26
            for letter in i:
                letterCnt[ord(letter) - ord('a')] +=1
            key=tuple(letterCnt)


            res[key].append(i)
        return (list(res.values()))





