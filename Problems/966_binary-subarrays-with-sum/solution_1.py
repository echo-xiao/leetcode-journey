class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        return self.atMost(nums, goal) - self.atMost(nums, goal-1)


    def atMost(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        left, right = 0, 0
        res = 0
        cnt = 0

        while right < len(nums):
            res += nums[right]
            right += 1

            while res > k:
                res -= nums[left]
                left += 1

            cnt += (right - left)

        return cnt
                