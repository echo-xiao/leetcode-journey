class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        max_len, sum_len1, sum_len2 = 0, 0, 0
        for i in range(0, len(nums)):
            
            if nums[i] in seen:
                seen[nums[i]] += 1
            elif nums[i] not in seen:
                seen[nums[i]] = 1

            if nums[i]-1 in seen:
                sum_len1 = seen[nums[i]] + seen[nums[i]-1]
            if nums[i]+1 in seen:
                sum_len2 = seen[nums[i]] + seen[nums[i]+1]
            max_len = max(max_len, sum_len1)
            max_len = max(max_len, sum_len2)
            
        return max_len
            