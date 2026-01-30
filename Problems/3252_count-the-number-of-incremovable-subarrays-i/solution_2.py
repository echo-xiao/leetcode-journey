class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                rem = nums[:i] + nums[j+1:]
                if self.if_increasing(rem):
                    cnt += 1
        return cnt

    def if_increasing(self, nums: List[int]) -> bool:
        for k in range(len(nums)-1):
            if nums[k] >= nums[k+1]:
                return False
        return True