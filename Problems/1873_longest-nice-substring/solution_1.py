class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        seen = set(s)
        if len(s) < 2:
            return ""


        for i in range(0, len(s)):
            if s[i].lower() not in seen or s[i].upper() not in seen:
                left = self.longestNiceSubstring(s[0:i])
                right = self.longestNiceSubstring(s[i+1:])
            
                if len(left) >= len(right):
                    return left
                else:
                    return right
        return s