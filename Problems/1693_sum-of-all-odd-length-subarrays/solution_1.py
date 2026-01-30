class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        curr = [0] * (n+1)

        for i in range(0, n):
            curr[i+1] = curr[i] + arr[i]

        res = 0
        for left in range(0, n):
            for right in range(left, n):
                length = right - left + 1
                if length % 2 == 1:
                    res += curr[right+1] - curr[left]
        return res

