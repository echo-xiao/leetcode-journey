class Solution:
    def minimumSum(self, num: int) -> int:
        nums = list(str(num))
        nums.sort()
        print(nums)
        return int(nums[0]) * 10 + int(nums[1]) * 10 + int(nums[2]) + int(nums[3])