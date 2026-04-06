class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        s1Map = defaultdict(int)
        for i in s1:
            s1Map[i] += 1

        s1MapTmp = s1Map.copy()

        l=0
        countRemaining = len(s1)
        for i,r in enumerate(s2):
            print(l)
            if r in s1MapTmp:
                # print(r)
                s1MapTmp[r] -= 1
                countRemaining -=1
                if s1MapTmp[r] < 0:
                    while s1MapTmp[r] < 0:
                        s1MapTmp[s2[l]] +=1
                        l +=1
                        countRemaining+=1
                elif s1MapTmp[r] == 0:
                    if countRemaining == 0:
                        return True


            else:
                l = i+1
                s1MapTmp = s1Map.copy()
                countRemaining = len(s1)

        return False

            
            


