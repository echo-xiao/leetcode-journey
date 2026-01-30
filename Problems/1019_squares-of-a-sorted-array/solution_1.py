class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        res = [0] * len(nums)
        i = 0
        j = len(nums)-1
        k = len(nums)-1

        while i <= j:
            if nums[i]**2 > nums[j]**2:
                res[k] = nums[i]**2
                i += 1
            elif nums[i]**2 <= nums[j]**2:
                res[k] = nums[j]**2
                j -= 1
            k -= 1
        return res
