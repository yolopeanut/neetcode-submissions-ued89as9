class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        l,r = 0, 1

        length = 1
        while r<len(s):
            if s[r] not in s[l:r]:
                length = max(length, len(s[l:r+1]))
                print(s[l:r+1])
            else:
                
                while s[r] in s[l:r] and l<r:
                    l+=1

            r+=1

        return(length)