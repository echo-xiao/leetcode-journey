class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0] * (n+1)

        for i in range(0, n):
            arr[i+1] = arr[i] + nums[i]
        return arr[1:]