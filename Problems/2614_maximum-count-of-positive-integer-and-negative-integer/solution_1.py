class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        curr = self.helper(nums, 0, len(nums)-1)

        neg = len(nums[0:curr])
        while curr < len(nums) and nums[curr] <= 0:
            curr += 1
        pos = len(nums[curr:])

        return max(pos, neg)
        
        

    def helper(self, nums: List[int], left: int, right: int) -> int:
        if left > right:
            return left

        mid = left + (right - left) // 2
        if nums[mid] >= 0:
            return self.helper(nums, left, mid-1)
        elif nums[mid] < 0:
            return self.helper(nums, mid+1, right)