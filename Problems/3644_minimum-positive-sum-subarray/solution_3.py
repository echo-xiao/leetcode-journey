class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        n = len(nums)
        curr = [0] * (n+1)

        for i in range(0, n+1):
            curr[i] = curr[i-1] + nums[i-1]

        res = 0
        min_res = float('inf')

        for left in range(0, n):
            for right in range(0, n):
                length = right - left + 1
                if length >= l and length <= r :
                    ttl = curr[right+1] - curr[left]
                    if ttl > 0:
                        min_res = min(min_res, ttl)
        if min_res != float('inf'):
            return min_res 
        else:
            return -1