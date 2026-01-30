class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = -1

        for i in range(0, len(nums)):
            left = i + 1
            right = len(nums)-1
            while left <= right:
                mid = left + (right - left) // 2
                sm = nums[mid] + nums[i]
                if sm < k:
                    res = max(sm, res)
                    left = mid + 1
                elif sm >= k:
                    right = mid - 1
        return res
