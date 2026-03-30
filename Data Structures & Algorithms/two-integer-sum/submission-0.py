class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = dict()
        for i, num in enumerate(nums):
            if target - num in num_dict:
                output = [i, num_dict[target-num]]
                output.sort()
                return output
            else: 
                num_dict[num] = i
                
        