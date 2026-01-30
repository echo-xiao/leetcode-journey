class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        pivot = self.findPivotIndex(nums)

        if nums[pivot] <= target <= nums[len(nums)-1]:
            return self.binarySearch(nums, pivot, len(nums)-1, target)
        else:
            return self.binarySearch(nums, 0, pivot-1, target)
    

    def findPivotIndex(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:                
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
                
        return left

    def binarySearch(self, nums: List[int], left, right, target):
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1