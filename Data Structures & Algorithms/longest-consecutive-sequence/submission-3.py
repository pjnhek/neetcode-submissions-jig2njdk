class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        nums = sorted(list(nums))
        print(nums)
        res = 1
        res_1 = 1
        for num in nums:
            if num + 1 in nums:
                res += 1
            else:
                if res >= res_1:
                    res_1 = res
                    res = 1
        return max(res, res_1)


