class Solution(object):
    def minimumSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        r = 0
        l = 0
        min_res = 10000000
        curr = 0
        
        for l in range(0, len(nums)):
            curr = 0
            for r in range(l, len(nums)):
                curr |= nums[r]
                if curr >= k:
                    res = r - l + 1
                    min_res = min(res, min_res)
                    break
        
        
        if min_res == 10000000:
            return -1
        else:
            return min_res
        
