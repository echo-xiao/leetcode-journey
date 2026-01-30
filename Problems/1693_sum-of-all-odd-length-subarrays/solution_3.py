class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        curr = [0] * (n+1)

        for i in range(0, n):
            curr[i+1] = curr[i] + arr[i]

        for i in range(0, n):
            for j in range(i, n):
                L = j - i + 1
                if L % 2 == 1:
                    ttl = curr[j+1] - curr[i]
                    res += ttl
        return res
