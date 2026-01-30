class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:

        maxRes = -1
        for i in range(0, len(nums)-k+1):
            if nums[i] > maxRes:
                maxRes = nums[i]
                idx = i
        return nums[idx: idx+k]