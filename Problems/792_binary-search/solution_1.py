class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums, target, 0, len(nums)-1)
        

    def helper(self, nums: List[int], target: int, left: int, right: int) -> int:

        if left > right:
            return -1

        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.helper(nums, target, left, mid-1)
        elif nums[mid] < target:
            return self.helper(nums, target, mid+1, right)
        