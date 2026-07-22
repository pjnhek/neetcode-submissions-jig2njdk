class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(nums):
            dic[n] = i
        for i, n in enumerate(nums):
            if target - n in dic.keys() and dic[target-n] != i:
                return [i, dic[target-n]]
        
        
        