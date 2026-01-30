class Solution(object):
    def incremovableSubarrayCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        l = 0
        r = n-1
        

        while l < n-1 and nums[l] < nums[l+1]:
                l += 1
        
        while r > 0 and nums[r-1] < nums[r]:
                r -= 1

        if l == n - 1:
            return n * (n + 1) // 2
            

        j = r
        cnt = (n-r+1)
    
        for i in range(l + 1):
            while j < n and nums[i] >= nums[j]:
                j += 1
            cnt += (n-j+1)
        return cnt
