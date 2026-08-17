class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        left, right = 0, n//2
        ops = 0
        while left < n//2 and right < n:
            if 2 * nums[left] <= nums[right]:
                ops += 2
                left += 1
                right += 1
            else:
                right += 1
        return ops