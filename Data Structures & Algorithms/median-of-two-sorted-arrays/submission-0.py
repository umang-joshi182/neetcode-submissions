class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if r % 2 != 0:
                return (nums[m] + nums[m + 1]) / 2
            else: 
                return nums[m]