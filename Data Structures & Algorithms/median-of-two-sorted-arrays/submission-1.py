class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1+nums2
        nums.sort()
        if len(nums)%2 == 0:
            mid = int(len(nums)/2)
            id1 = nums[mid]
            id2 = nums[mid-1]
            return (id1+id2)/2
        else:
            return int(nums[len(nums)//2])