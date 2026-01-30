class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        right = k-1
        left = 0
        msum = -1000000
        ksum = float(sum(nums[left: right+1]))
        msum = ksum

        for right in range(k, len(nums)):
            ksum = float(ksum + nums[right] - nums[left])
            msum = max(msum, ksum)
            left = left + 1
        return float(msum / k)