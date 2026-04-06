class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charArrS = 26*[0]
        charArrT = 26*[0]

        for char in s:
            index = ord(char)-ord('a')
            charArrS[index] +=1 

        for char in t:
            index = ord(char)-ord('a')
            charArrT[index] +=1 

        for i in range(len(charArrS)):
            if charArrS[i] != charArrT[i]:
                return False
        
        return True
        
        
            
    