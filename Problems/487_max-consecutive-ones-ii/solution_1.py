class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = {}
        left, right = 0, 0
        maxLen = 0
        res = []

        while right < len(nums):
            cnt[nums[right]] = 1 + cnt.get(nums[right], 0)
            right += 1
            
            while cnt.get(0, 0) > 1:
                cnt[nums[left]] -= 1
                left += 1
            maxLen = max(maxLen, right-left)
        return maxLen
            
