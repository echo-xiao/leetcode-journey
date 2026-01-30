class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_set = set()
        num = 0
        max_num = -1
        for i in range(0, len(nums)):
            my_set.add(-nums[i])

        for j in range(0, len(nums)):
            num = nums[j]
            if num in my_set:
                max_num = max(num, max_num)
        return max_num