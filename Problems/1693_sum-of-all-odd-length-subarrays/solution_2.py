class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0

        for i, val in enumerate(arr):
            left = i + 1
            right = n - i
            ttl = left * right
            cnt = math.ceil(ttl/2)
            res += val * cnt
        return res