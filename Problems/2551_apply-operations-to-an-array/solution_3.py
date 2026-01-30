class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        j = 0 

        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0
            
        
        for i in nums:
            if i != 0:
                res.append(i)

        zeros = len(nums) - len(res)
        res.extend([0] * zeros)
        return res
    