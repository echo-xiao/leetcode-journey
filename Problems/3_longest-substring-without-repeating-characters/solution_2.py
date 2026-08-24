class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        win = {}
        i = 0
        maxres = 0
        n = len(s)
        for j in range(0, n):
            c = s[j]
            if c not in win:
                win[c] = 1
            else:
                win[c] += 1
            
            while win[c] > 1:
                left = s[i]
                win[left] -= 1
                i += 1

            res = j-i+1
            maxres = max(res, maxres)
        return maxres