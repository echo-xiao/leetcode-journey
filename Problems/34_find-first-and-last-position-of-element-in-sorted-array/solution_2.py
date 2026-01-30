class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        firstBound = self.findBound(nums, target, isFirst = True)

        if firstBound == -1:
            return [-1, -1]

        lastBound = self.findBound(nums, target, isFirst = False)

        return [firstBound, lastBound]


    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:
        left, right = 0, len(nums)-1
        candidate = -1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                candidate = mid
                if isFirst == True:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return candidate