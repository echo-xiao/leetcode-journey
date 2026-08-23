class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        maxlen = 1
        length = 1
        
        if not nums:
            return 0
        for i in range(0, len(nums)):
            if nums[i] == nums[i-1]:
                pass
            elif nums[i] == nums[i-1] + 1:
                length += 1
                maxlen = max(length, maxlen)
            else:
                length = 1
        return maxlen