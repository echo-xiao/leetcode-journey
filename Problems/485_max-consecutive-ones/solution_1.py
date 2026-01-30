class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        
        result, cnt = 0, 0
        for n in nums:
            if n == 1:
                cnt += 1
            else:
                result = max(result, cnt)
                cnt = 0
        return max(result, cnt)