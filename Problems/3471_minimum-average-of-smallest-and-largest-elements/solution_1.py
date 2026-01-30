class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        
        nums.sort()
        n = len(nums)
        i = 0
        j = n-1
        avg = []
        num = 0

        while i < j:
            num = (nums[i] + nums[j]) / 2.0
            avg.append(num)
            i += 1
            j -= 1
        return min(avg)