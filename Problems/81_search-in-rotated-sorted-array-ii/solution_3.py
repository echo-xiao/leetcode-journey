class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        pivot = self.findPivotIndex(nums)
        return self.binarySearch(nums, 0, pivot - 1, target) or self.binarySearch(nums, pivot, len(nums) - 1, target)

    def findPivotIndex(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # if left == right:
            #     return left
                
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                if right > 0 and nums[right] < nums[right - 1]:
                    return right
                right -= 1
                
        return 0


    def binarySearch(self, nums: List[int], left: int, right: int, target: int) -> bool:
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False