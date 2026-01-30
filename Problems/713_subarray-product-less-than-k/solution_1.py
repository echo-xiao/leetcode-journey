class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        left, right = 0, 0
        res = 1
        ans = 0
        while right < len(nums):
            res *= nums[right]
            right += 1
            
            while res >= k:
                res //= nums[left]
                left += 1

            ans += (right-left)
        return ans