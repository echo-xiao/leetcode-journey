class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        n = len(nums)
        j = 1
        k = 2
        cnt = 0

        for i in range(0, n-2):
            j = max(j, i+1)
            while j < n and nums[j] < nums[i] + diff:
                j += 1
            if j >= n or nums[j] > nums[i] + diff:
                continue
            
            k = max(k, j+1)
            while k < n and nums[k] < nums[i] + 2 * diff:
                k += 1
            if k >= n:
                break

            if nums[k] == nums[j] + diff:
                cnt += 1
        return cnt