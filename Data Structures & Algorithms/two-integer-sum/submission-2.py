class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dic = {}
        for i, n in enumerate(nums):
            num_dic[n] = i
        for i, n in enumerate(nums):
            search = target - n
            if search in num_dic.keys() and num_dic[search] != i:
                return [i, num_dic[search]]