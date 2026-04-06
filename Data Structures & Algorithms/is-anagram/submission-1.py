class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        resArr = [0] * 26
        resArr2 = [0] * 26
        if(len(s) != len(t)):
            return False

        for i in s:
            index = ord(i) - ord('a')
            print(i, index)
            resArr[index] += 1
        
        for i in t:
            index = ord(i) - ord('a')
            print(i, index)
            resArr2[index] += 1
        
        print(resArr,'/n',resArr2)


        if resArr!=resArr2:
            
            return False

        return True

