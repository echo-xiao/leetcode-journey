class Solution(object):
    def minimumSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        l = 0 
        res = 0
        min_len = float('inf')
        

        for l in range(0, len(nums)):
            res = 0
            for r in range(l, len(nums)):
                res = res | nums[r]
                if res >= k:
                    min_len = min(min_len, r - l + 1)
                    break
                
        if min_len == float('inf'):
            return -1
        else:
            return min_len
