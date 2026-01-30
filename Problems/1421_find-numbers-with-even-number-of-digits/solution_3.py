class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                cnt += 1
        return cnt 