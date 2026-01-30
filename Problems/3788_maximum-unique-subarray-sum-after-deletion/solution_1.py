class Solution:
    def maxSum(self, nums: List[int]) -> int:
        arr = set(nums)
        res = 0
        maxVal = max(arr)

        if maxVal > 0:
            for i in arr:
                if i >= 0:
                    res += i
            return res

        else:
            return maxVal