class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = [0] * 26
        for i in s:
            letter_int = ord(i)-ord('a')
            res[letter_int] += 1

        for i in t:
            letter_int = ord(i)-ord('a')
            res[letter_int] -= 1

        for i in res:
            if i != 0:
                return False

        return True