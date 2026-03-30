class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        suff = [0] * n
        pref[0] = suff[n-1] = 1
        for i in range(1, n):
            pref[i] = pref[i-1] * nums[i-1]
        for s in range(n-2, -1, -1):
            suff[s] = suff[s+1] * nums[s+1]
        res = []
        for i, s in zip(pref, suff):
            res.append(i*s)
        return res 
