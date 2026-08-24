class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for ch in t:
            if ch not in need:
                need[ch] = 1
            else:
                need[ch] += 1
            
        i = 0
        basei = 0
        minres = float('inf')
        n = len(s)
        win = {}

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
                    basei = i

                left = s[i]
                win[left] -= 1
                if win[left] == 0:
                    del win[left]
                i+=1

        if minres == float('inf'):
            return ""
        return s[basei: basei + minres]

    def covered(self, win, need):
        for ch in need:
            if ch not in win:
                return False
            if win[ch] < need[ch]:
                return False
        return True