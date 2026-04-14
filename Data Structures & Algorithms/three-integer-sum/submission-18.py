class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        [-1,-1,1,0]
        # we dont care for the last 2 index
        for i in range(len(nums)-2):
            # skip duplicates 
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # left pointer
            left = i + 1
            # right pointer 
            right = len(nums)-1
            while left < right:
                curr = nums[i] + nums[left] + nums[right]
                if curr == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif curr < 0:
                    left += 1
                else:
                    right -= 1
        return res

            



