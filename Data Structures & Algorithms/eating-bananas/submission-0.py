class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        
        l = 1
        r = max(piles) # 4

        min_mp_rate = r
        while l<=r:
            mp_rate = (l+r)//2 #2
            total_num_turns = 0
            for i in piles:
                total_num_turns += -(-i//mp_rate)

            if total_num_turns<=h:
                min_mp_rate = mp_rate

                # try moving r to mp-1
                r = mp_rate-1

            
            elif total_num_turns>h:
                l = mp_rate+1

        return min_mp_rate

             

            

            



            