class Solution(object):
    def twoSumLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        i, j = 0, 1
        n = len(nums)
        sum_num, max_num = -1, -1
        
        while i < n:
            while j < n:
                sum_num = nums[i] + nums[j] 
                if sum_num < k:
                    max_num = max(sum_num, max_num)
                j += 1
            i += 1
            j = i + 1

        if max_num > 0:
            return max_num
        else:
            return -1

            