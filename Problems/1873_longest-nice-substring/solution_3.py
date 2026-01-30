class Solution(object):
    def longestNiceSubstring(self, s):
        seen = {}

        if len(s) < 2:
            return ""

        for char in s:
            lower = char.lower()
            upper = char.upper()

            if lower not in seen:
                seen[lower] = [False, False]
            
            if char.islower():
                seen[lower][0] = True
            else:
                seen[lower][1] = True

        for i, v in enumerate(s):
            if seen[v.lower()] in ([False, True], [True, False]):
                left = s[0: i]
                right = s[i+1: len(s)]

                res_left = self.longestNiceSubstring(left)
                res_right = self.longestNiceSubstring(right)
            
                if len(res_left) >= len(res_right):
                    return res_left
                else:
                    return res_right

        return s





            