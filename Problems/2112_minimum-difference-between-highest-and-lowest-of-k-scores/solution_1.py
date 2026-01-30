class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        

        nums.sort()

        j = 0
        min_diff = 10000000

        for i in range(k-1, len(nums)):
            win = nums[j: i+1]
            diff = nums[i] - nums[j]
            if diff < min_diff:
                min_diff = min(diff, min_diff)
            j += 1
        return min_diff