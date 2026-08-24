class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       
        n = len(s)
        win = {}
        i = 0
        maxres = 0

        for j in range(0, n):
            c = s[j]
            if c not in win:
                win[c] = 1
            else:
                win[c] += 1
            
            maxcnt = 0
            for ch in win:
                if win[ch] > maxcnt:
                    maxcnt = win[ch]
            need = (j-i+1) - maxcnt
            
            while need > k:
                left = s[i]
                win[left] -= 1
                if win[left] == 0:
                    del win[left]
                i += 1

                maxcnt = 0
                for ch in win:
                    if win[ch] > maxcnt:
                        maxcnt = win[ch]
                need = (j-i+1) - maxcnt
            
            res = j - i + 1
            maxres = max(res, maxres)
        return maxres
