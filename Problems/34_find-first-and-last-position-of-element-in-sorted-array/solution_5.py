class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1

        firstBound, lastBound = -1, -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                firstBound = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                lastBound = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1       


        return [firstBound, lastBound]

