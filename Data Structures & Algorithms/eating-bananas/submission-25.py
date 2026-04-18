class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right 
        while left <= right:
            k = left + ((right-left)//2)
            val = 0
            for p in piles:
                val += (p+k-1)//k
            if val <= h:
                ans = k
                right = k - 1
            else:
                left = k + 1
        return ans
        
            

        

