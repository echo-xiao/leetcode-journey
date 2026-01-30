class Solution:
    def pivotInteger(self, n: int) -> int:
        nums = list(range(1, n+1))
        arr = [0] * (n+1)

        for i in range(0, n):
            arr[i+1] = arr[i] + nums[i]

        for j in range(1, n+1):
            if arr[j] == arr[-1] - arr[j-1]:
                return j
        return -1


