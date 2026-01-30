class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        j = 1
        while i < len(nums) and j < len(nums):
            if nums[i] % 2 != 0 and nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j += 2
            elif nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 != 0:
                j += 2
        return nums
                