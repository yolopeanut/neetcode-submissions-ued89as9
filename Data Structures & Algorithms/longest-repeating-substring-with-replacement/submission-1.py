class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1

        sMap = defaultdict(int)

        l = 0
        max_len = 0
        max_freq_in_window = 0

        # Starts at 0
        for r in range(len(s)):
            sMap[s[r]] += 1

            max_freq_in_window = max(max_freq_in_window, sMap[s[r]])
            window_len = r-l+1

            if(window_len-max_freq_in_window)>k:
                sMap[s[l]] -=1
                l+=1

            window_len = r-l+1
            max_len = max(max_len,window_len)
        return max_len



            




