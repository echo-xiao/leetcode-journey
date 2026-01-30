class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        ind = []
        res = []

        for i in range(0, len(nums)):
            if nums[i] == key:
                ind.append(i)

        for i in range(0, len(nums)):
            for j in range(0, len(ind)):
                num = abs(i - ind[j])
                if num <= k:
                    res.append(i)
                    break
        return res