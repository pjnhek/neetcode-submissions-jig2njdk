class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we want to use a sliding window to find the longest substring without repeating
        # char. to do this, everytime we move our right pointer, we add that right pointer
        # to a set. if the right pointer is in the set, we move the left pointer until it's
        # the same char as right pointer and remove it from the set, then we add the new
        # right pointer to the set and move on

        l, tracker = 0, set()
        maxChar = 0
        for r in range(len(s)):
            while s[r] in tracker:
                tracker.remove(s[l])
                l += 1
            maxChar = max(maxChar, r-l+1)
            tracker.add(s[r])
        return maxChar


            

            
            
