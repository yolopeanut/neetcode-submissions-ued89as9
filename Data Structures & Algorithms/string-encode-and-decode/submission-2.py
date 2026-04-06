class Solution:

    def encode(self, strs: List[str]) -> str:
      
        test =  [f'{len(s)}#{s}' for s in strs]
        print(''.join(test))
        return ''.join(test)


    def decode(self, s: str) -> List[str]:
        res = []
        currIndex = 0

        while(currIndex < len(s)-1):
            lenCurrStr = ''
            while s[currIndex].isdigit():
                lenCurrStr += s[currIndex]
                currIndex+=1
            
            # For delim skipping
            currIndex+=1

            endingIndx= currIndex+int(lenCurrStr)
            res.append(s[currIndex:endingIndx])
            print(res)

            currIndex+=int(lenCurrStr)
        return res
            
            
