class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i, n in enumerate(nums):
            dic[n] = i
        for i, n in enumerate(nums):
            found = target - n
            if found in dic.keys() and i != dic[found]:
                return [i, dic[found]]
        return []