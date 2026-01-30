class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        cnt = 0
        res = 0
        for i in range(0, len(nums)):
            cnt += nums[i]
            if cnt == 0:
                res += 1
        return res