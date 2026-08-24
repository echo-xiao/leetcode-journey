class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = {}
        for i in s1:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1
        

        win = {}
        n = len(s1)
        for j in range(0,len(s2)):
            c = s2[j]
            if c not in win:
                win[c] = 1
            else:
                win[c] += 1

            if j >= n:
                left = s2[j-n]
                win[left] -= 1
                if win[left] == 0:
                    del win[left]
            
            if seen == win:
                return True
        return False