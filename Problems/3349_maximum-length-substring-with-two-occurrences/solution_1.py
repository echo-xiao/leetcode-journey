class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        max_length = 0
        seen = {}


        for r in range(0, len(s)):
            if s[r] not in seen:
                seen[s[r]] = 1
            else:
                seen[s[r]] += 1
            
            while seen[s[r]] > 2:
                seen[s[l]] -= 1
                l += 1
        
            length = r - l + 1
            max_length = max(length, max_length)

        return max_length

