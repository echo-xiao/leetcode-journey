class Solution(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max_res = 0

        for r in range(0, len(nums)):
            for l in range(0, r):
                if nums[r] <= nums[l] * 2:
                    res = nums[l] ^ nums[r]
                    max_res = max(res, max_res)

        return max_res
