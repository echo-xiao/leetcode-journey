class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        maxlen = 0
        for i in seen:
            if i-1 in seen:
                continue
            length = 1
            cur = i
            while cur+1 in seen:
                length += 1
                cur += 1
            maxlen = max(maxlen, length)
        return maxlen