class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()

        left = self.helper(nums, target, 0, len(nums)-1)
        res = []
        while left < len(nums) and nums[left] == target:
            res.append(left)
            left += 1
        return res
        
    def helper(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left > right:
            return left
        
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            return self.helper(nums, target, left, mid-1)
        elif nums[mid] < target:
            return self.helper(nums, target, mid+1, right)