class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        

        i = 0
        while k > 0:
            nums.sort()
            nums[0] = -nums[0]
            k -= 1
        return sum(nums)