class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        curr = [0] * (n+1)

        for i in range(1, n+1):
            curr[i] = curr[i-1] + nums[i-1]

        res = 0
        ttl = 0
        for end in range(n):
            start = max(0, end - nums[end])

            ttl += curr[end+1] - curr[start]
            res += ttl
        return ttl