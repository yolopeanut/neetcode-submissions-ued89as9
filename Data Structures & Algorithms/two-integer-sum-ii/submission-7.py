class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # lptr and rptr minus, compare with target. 
        # list is sorted, so just increase or decrease accordingly

        # lptr = 0
        # rptr = len(numbers)-1

        # while lptr<rptr:
        #     sumResult = numbers[rptr] + numbers[lptr] 
        #     if sumResult == target:
        #         return [lptr+1,rptr+1]
                
        #     elif sumResult > target:
        #         rptr -= 1

        #     elif sumResult < target:
        #         lptr += 1


        prevMap = {}

        for i,n in enumerate(numbers):
            diff = target-n

            if diff in prevMap:
                return [prevMap[diff]+1,i+1]

            prevMap[n] = i
        
        print(prevMap)

        return []


            