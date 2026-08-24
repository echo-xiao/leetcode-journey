class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = {}
        for i in s1:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1

        k = len(s1)
        win = {}

        for i in range(0, len(s2)):
            c = s2[i]
            if c not in win:
                win[c] = 1
            else:
                win[c] += 1



            if i >= k:
                out = s2[i-k]
                win[out] -= 1
                if win[out] == 0:
                    del win[out]
            
            if win == seen:
                return True

                

        return False
            