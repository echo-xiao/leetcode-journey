class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        win = set()
        i = 0
        maxres = 0
        n = len(s)

        for j in range(0, n):
            c = s[j]
            while c in win:
                left = s[i]
                win.remove(left)
                i += 1
            win.add(c)
            res = j-i+1
            maxres = max(res, maxres)
        return maxres