class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        s1Map = defaultdict(int)
        for i in s1:
            s1Map[i] += 1

        lenWin = len(s1)

        for i in range(len(s2)-lenWin+1):
            s2WindowMap = defaultdict(int)
            print(s2[i:i+lenWin])
            for j in s2[i:i+lenWin]:
                s2WindowMap[j] += 1
            
            if s1Map == s2WindowMap:
                return True

        return False


            
            


