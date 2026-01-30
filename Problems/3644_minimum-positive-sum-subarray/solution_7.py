class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        
        n = len(nums)
        min_sum = float('inf')

        for size in range(l, r+1):
            
            for i in range(0, n-size+1):
                res = sum(nums[i: i+size])
                if res > 0:
                    min_sum = min(res, min_sum)
                
        if min_sum == float('inf'):
            return -1
        else:
            return min_sum
                
