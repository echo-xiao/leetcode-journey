class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
    
        m = len(nums) // 2

        if not nums:
            return 0

        if nums[m] == target:
            return m
        elif nums[m] > target:
            return self.searchInsert(nums[0:m], target)
        elif nums[m] < target:
            return self.searchInsert(nums[m+1:], target) + (m+1)
    