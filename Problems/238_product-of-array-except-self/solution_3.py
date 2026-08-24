class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        left, right = 1, 1

        for i in range(1, len(nums)):
            left *= nums[i-1]
            res[i] = left

        for j in range(len(nums)-2, -1, -1):
            right *= nums[j+1]
            res[j] *= right
        
        return res