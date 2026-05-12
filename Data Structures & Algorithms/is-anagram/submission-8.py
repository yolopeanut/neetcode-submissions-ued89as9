class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        res = [0] * 26
        for i in range(len(s)):
            letter_int_s = ord(s[i])-ord('a')
            res[letter_int_s] += 1

            letter_int_t = ord(t[i])-ord('a')
            res[letter_int_t] -= 1

        for i in res:
            if i !=0:
                return False
        
        return True
      