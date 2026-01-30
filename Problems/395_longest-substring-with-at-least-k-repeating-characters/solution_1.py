class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        if len(s) < k:
            return 0

        dic = {}

        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1

        maxRes = 0

        for key, val in dic.items():
            if val < k:
                subStrings = s.split(key)

                maxRes = 0
                for cut in subStrings:
                    res = self.longestSubstring(cut, k)
                    maxRes = max(res, maxRes)
                return maxRes
        return len(s)
