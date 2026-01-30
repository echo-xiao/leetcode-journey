class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i = 0
        j = 0
        res = []

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                res.append(s[i])
                i += 1
            j += 1
        
        return len(s) == len(res)