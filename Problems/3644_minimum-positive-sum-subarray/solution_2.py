class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        n = len(nums)
        curr = [0] * (n+1)

        for i in range(0, n+1):
            curr[i] = curr[i-1] + nums[i-1]

        res = inf
        for left in range(0, n - l + 1):
            for right in range(left + l, min(left + r, n) + 1):
                ttl = curr[right] - curr[left]
                if ttl > 0:
                    res = min(res, ttl)
        if res == inf:
            return -1
        else:
            return res
