class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        cnt = 0
        for i in range(0, len(nums)):
            if nums[i] == target:
                cnt += 1
        if cnt > len(nums) / 2:
            return True
        else:
            return False