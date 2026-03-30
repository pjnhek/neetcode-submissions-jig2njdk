class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(set(nums))
        while n > k:
            for i in set(nums):
                if i in nums:
                    nums.remove(i)
                    n = len(set(nums))
                else:
                    continue
        return list(set(nums))
            
            
            
