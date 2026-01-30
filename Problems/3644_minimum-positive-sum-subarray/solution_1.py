class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        n = len(nums)
        curr = [0] * (n+1)

        for i in range(0, n+1):
            curr[i] = curr[i-1] + nums[i-1]

        res = inf
        for length in range(l, r+1):
            for left in range(0, n-length + 1):
                right = left + length - 1
                ttl = curr[right+1] - curr[left]
                if ttl > 0:
                    res = min(res, ttl)

        if res == inf:
            return -1
        else:
            return res