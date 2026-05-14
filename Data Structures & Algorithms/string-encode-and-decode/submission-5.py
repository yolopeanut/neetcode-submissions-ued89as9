class Solution:
    # 6hello66world/
    def encode(self, strs: List[str]) -> str:
        res = ""
        sentence  = res.join(f"{len(w)}#{w}" for w in strs)
        print(sentence)
        return sentence

    # 5#Hello5#World
    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        currIndex = 0

        while currIndex <len(s):
            currNum = ''

            while s[currIndex] != '#':
                currNum += s[currIndex]
                currIndex +=1
            
            currIndex +=1

            currStr = s[currIndex: currIndex + int(currNum)]
            print(currStr)
            res.append(currStr)
            currIndex += int(currNum)
        print(res)
            


        return res
        
        
