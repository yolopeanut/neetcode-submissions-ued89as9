class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numDict = defaultdict(int)

        for i in range(len(numbers)):
            complementary = target-numbers[i]

            # If complementary's key exists
            if numDict[complementary]:
                return [numDict[complementary],i+1]
            
            # storing number as key, index +1 as value
            numDict[numbers[i]] = i+1
        
        return []
