class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            countLetters = [0] * 26

            for char in string:
                countLetters[ord(char)-ord('a')] += 1

            res[tuple(countLetters)].append(string)

            
        return list(res.values())