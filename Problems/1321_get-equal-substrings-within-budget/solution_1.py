class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        left, right = 0, 0
        ttl = 0
        maxlen = 0

        for right in range(0, len(s)):
            ttl += abs(ord(s[right]) - ord(t[right]))
            while ttl > maxCost:
                ttl -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            maxlen = max(maxlen, right-left+1)
        return maxlen