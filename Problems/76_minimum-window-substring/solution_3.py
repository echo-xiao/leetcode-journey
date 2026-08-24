class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        n = len(s)
        win = {}
        i = 0
        need = {}

        for ch in t:
            if ch not in need:
                need[ch] = 1
            else:
                need[ch] += 1

        minres = float('inf')
        besti = 0
         
        for j in range(0, n):
            c = s[j]
            if c not in win:
                win[c] = 1
            else:
                win[c] += 1

            while self.covered(win, need) is True:
                res = j - i + 1
                if res < minres:
                    minres = res
                    besti = i

                left = s[i]
                win[left] -= 1
                if win[left] == 0:
                    del win[left]
                i += 1
        
        if minres == float('inf'):
            return ""
        return s[besti: besti + minres]


    def covered(self, win, need):
        for x in need:
            if x not in win:
                return False
            if win[x] < need[x]:
                return False
        return True