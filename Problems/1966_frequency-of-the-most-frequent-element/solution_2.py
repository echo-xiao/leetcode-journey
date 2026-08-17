class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left, righ = 0, 0
        maxlen = 0
        ttl = 0
        
        for right in range(0, n):
            ttl += nums[right]
            cost = nums[right] * (right-left+1) - ttl
            while cost > k:
                ttl -= nums[left]
                left += 1
                cost = nums[right] * (right-left+1) - ttl
            maxlen = max(maxlen, right-left+1)
        return maxlen

            