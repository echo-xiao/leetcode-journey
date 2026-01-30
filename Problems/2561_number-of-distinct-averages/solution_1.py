class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        my_set = set()

        i, j = 0, len(nums)-1
        while i < j:
            min_num = nums[i]
            max_num = nums[j]
            avg_num = (min_num + max_num) / 2.0
            my_set.add(avg_num)
            i += 1
            j -= 1
        return len(my_set)