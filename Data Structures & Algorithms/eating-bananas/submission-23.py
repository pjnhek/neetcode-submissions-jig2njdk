class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right
        while left < right:
            k = left + ((right-left)//2)
            print(k)
            val = 0
            for p in piles:
                if p%k != 0:
                    val += (p//k)+1
                else:
                    val += (p//k)
            print(val)
            if val <= h:
                ans = k
                right = k
            else:
                left = k + 1
            print(left, right)
        return ans

        

