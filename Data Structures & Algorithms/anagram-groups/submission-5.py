class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        val = defaultdict(list)
        for string in strs:
            arr = [0] * 26

            for letter in string:
                letter_int = ord(letter) - ord('a')
                arr[letter_int] += 1

            val[tuple(arr)].append(string)

        res = []
        for i in val.values():
            res.append(i)
            
        return res

