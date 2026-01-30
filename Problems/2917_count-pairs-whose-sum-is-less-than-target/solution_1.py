class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        i, j, cnt = 0, len(nums)-1, 0

        while i < j:
            if nums[i] + nums[j] < target:
                cnt += (j-i)
                i += 1
            elif nums[i] + nums[j] >= target:
                j -= 1
        return cnt