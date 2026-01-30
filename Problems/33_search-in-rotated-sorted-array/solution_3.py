class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1

        left, right = 0, n-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                pivot = mid
                right = mid - 1

        if nums[pivot] <= target <= nums[n-1]:
            return self.binarySearch(nums, pivot, n-1, target)
        else:
            return self.binarySearch(nums, 0, pivot-1, target)
    
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