class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        maxlen = 0
        for j in seen:
            if j-1 not in seen:
                length = 1
                cur = j
                while cur + 1 in seen:
                    length += 1
                    cur += 1
                maxlen = max(maxlen, length)
        return maxlen