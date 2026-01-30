class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= 0:
                right = mid-1
            else:
                left = mid+1

        neg = len(nums[0:left])
        while left < len(nums) and nums[left] <= 0:
            left += 1
        pos = len(nums[left:])

        return max(neg, pos)
