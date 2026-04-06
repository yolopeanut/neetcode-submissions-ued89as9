class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        if len(t) > len(s):
            return ""

        # Both should be maps, 
        have, need = defaultdict(int), defaultdict(int)
        haveC, needC = 0,0
        resIndex = [-1,-1]
        resLen = 10000
        
        for i in t:
            need[i] += 1
        needC = len(t)


        l = 0
        for r, e in enumerate(s):
            if e in need:
                have[e] += 1

                if have[e] <= need[e]:
                    haveC +=1

                while haveC == needC:
                    # update resIndex and resLen (max)
                    if r-l < resLen:
                        resIndex = [l,r]
                        resLen = r-l
                    
                    
                    if s[l] in have:
                        have[s[l]] -= 1
                        if have[s[l]] < need[s[l]]:
                            haveC -=1
                    
                    l+=1

        return(s[resIndex[0]:resIndex[1]+1])
        print(resIndex)
                    
                    
                
                



