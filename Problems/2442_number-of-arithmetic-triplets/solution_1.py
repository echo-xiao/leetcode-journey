class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        my_set = set()
        cnt = 0
        
        for i in range(0, len(nums)):
            my_set.add(nums[i])

        for j in range(0, len(nums)):
            a = nums[j]
            b = nums[j] + diff
            c = nums[j] + diff * 2
            if a in my_set and b in my_set and c in my_set:
                cnt += 1
        return cnt
            