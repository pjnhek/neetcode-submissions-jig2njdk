class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we know that the original array is sorted in ascending order
        # we need to find the range of the array 
        # we can do this by looking at the left and last val and the len of the array
        left = 0
        right = len(nums)-1
        if nums[left] < nums[right] or left == right:
            ans = nums[left]
            return ans
        else:
            ans = nums[right]
            while left <= right:
                mid = left + ((right-left)//2)
                if nums[mid] < ans:
                    ans = nums[mid]
                    right = mid - 1
                else:
                    left = mid + 1
        return ans
