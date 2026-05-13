class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window method, window is valid as long as:
        # window size - number of most frequent char <= k
        # update max substring while window is valid, and increase to right
        # if condition failed then shrink from left until valid and then go right again
        l, maxS = 0, 0
        char_counter = {}
        for r in range(len(s)):
            char_counter[s[r]] = char_counter.get(s[r], 0) + 1
            window = r - l + 1
            maxF = max(char_counter.values())
            while window - maxF > k:
                char_counter[s[l]] -= 1
                l += 1
                window = r - l + 1
                maxF = max(char_counter.values())
            maxS = max(maxS, window)
        return maxS

        
        
                
                    







