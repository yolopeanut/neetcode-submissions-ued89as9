class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Hint 1: First create a frequency map like before
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
        

        
        # Hint 2: Create bucket array
        # Why length of nums + 1? Think about max possible frequency
        freq = [[] for i in range(len(nums) + 1)]
        
        # Hint 3: Place numbers in buckets
        # For each number and its count in your frequency map:
        #   - Which index in freq should each number go?
        #   - freq[count] = number with that count
        for num, count in count.items():
            freq[count].append(num)

        print(freq)
        
        # Hint 4: Collect k most frequent
        result = []
        # Start from end of freq (highest frequencies)
        # Work backwards until you have k numbers
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                print(freq[i])
                # ... collect numbers ...
                result.append(n)
                # ... but only up to k numbers ...
                if len(result) == k:
                    return result