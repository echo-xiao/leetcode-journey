class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left, right = 0, 0
        cnt, maxlen = 0, 0

        for right in range(0, len(s)):
            if s[right] == s[right-1] and right > 0:
                cnt += 1
            while cnt > 1:
                if s[left] == s[left+1]:
                    cnt -= 1
                left += 1
            maxlen = max(maxlen, right-left+1)
        return maxlen