class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
        
        while left < len(nums) and nums[left] == target:
            res.append(left)
            left += 1
        return res
