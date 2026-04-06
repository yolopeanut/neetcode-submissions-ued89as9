class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = "".join(sorted(s))
        t = "".join(sorted(t))

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] == t[i]:
                continue
            else:
                return False
        
        return True