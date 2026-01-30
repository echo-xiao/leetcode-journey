class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)

        ttl = sum(nums)
        arr = [0] * (len(nums) + 1)

        for i in range(1, len(nums)+1):
            arr[i] = nums[i-1]+arr[i-1]
            if arr[i] > ttl - arr[i]:
                return nums[0: i]
            

        