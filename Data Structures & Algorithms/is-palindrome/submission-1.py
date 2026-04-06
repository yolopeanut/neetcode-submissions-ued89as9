class Solution:
    def isPalindrome(self, s: str) -> bool:
        singleWordLower = ''.join(s.split()).lower()
        cleanString = ''.join([i for i in singleWordLower if i.isalnum()])
        print(cleanString)

        lPtr = 0
        rPtr = len(cleanString)-1

        while(lPtr < rPtr):
            if(cleanString[lPtr]!= cleanString[rPtr]):
                return False
            
            lPtr +=1
            rPtr -=1

        return True
        