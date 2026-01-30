
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums)-1

        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            
            mid = left + (right - left) // 2
            res = min(res, nums[mid])
            if nums[mid] > nums[left]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid
            elif nums[mid] == nums[left]:
                left += 1

        return res