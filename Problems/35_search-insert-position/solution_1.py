class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.searchHelper(nums, target, 0, len(nums)-1)

    def searchHelper(self, nums: List[int], target: int, left: int, right: int) -> int:

        if left > right:
            return left


        mid = left + (right - left + 1) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.searchHelper(nums, target, left, mid-1)
        elif nums[mid] < target:
            return self.searchHelper(nums, target, mid+1, right)
        


        
    