class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        maxlen = 0
        left, right = 0, 0

        for right in range(0, n):
            while abs(nums[right] - nums[left]) > 2 * k:
                left += 1
            maxlen = max(maxlen, right-left+1)
        return maxlen