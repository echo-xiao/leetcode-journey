class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        return self.helper(nums, 0, len(nums)-1)

    def helper(self, nums: List[int], left: int, right: int) -> int:
        mid = left + (right - left) // 2
        if left > right:
            return left

        if nums[mid] == mid:
            return self.helper(nums, mid+1, right)
        elif nums[mid] > mid:
            return self.helper(nums, left, mid-1)
        

            