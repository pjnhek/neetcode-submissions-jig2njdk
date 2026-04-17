class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len_list = len(nums)
        list_dic = {}
        for i, n in enumerate(nums):
            list_dic[n] = i
        if len_list != len(list_dic):
            return True
        else:
            return False