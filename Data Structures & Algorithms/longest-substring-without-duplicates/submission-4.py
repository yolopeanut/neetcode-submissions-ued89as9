class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for i, char in enumerate(s):
            while char in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(char)
            res = max(res, i-l+1)

        return(res)



            
