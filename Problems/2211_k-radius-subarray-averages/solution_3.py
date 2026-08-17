class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = [-1] * len(nums)
        if 2 * k + 1 > len(nums):
            return res
        num = sum(nums[0: 2*k+1])
        res[k] = num // (2*k+1)
        for i in range(k+1, len(nums)-k):
            num += nums[i+k] - nums[i-k-1]
            res[i] = num // (2*k+1)
        return res