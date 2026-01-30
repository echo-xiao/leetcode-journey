class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        curr = [0] * (len(nums)+1)
        for i in range(0, len(nums)):
            curr[i+1] = curr[i] + nums[i]

        if min(curr) < 0:
            return 1 - min(curr) 
        else:
            return 1
