class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        

        leftBound = self.leftBound(nums, target)
        rightBound = self.rightBound(nums, target)

        return [leftBound, rightBound]

    def leftBound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if left < 0 or left >= len(nums):
            return -1 
        if nums[left] == target:
            return left
        else:
            return -1

    def rightBound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if right < 0 or right >= len(nums):
            return -1
        if nums[right] == target:
            return right
        else:
            return -1
