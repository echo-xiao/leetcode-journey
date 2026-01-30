class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return (nums[0] + nums[0] + k - 1) * k // 2