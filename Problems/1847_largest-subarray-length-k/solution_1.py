class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:

        maxVal = max(nums[0: len(nums)-k+1])
        idx = nums.index(maxVal)
        return nums[idx: idx+k]