class Solution:
    def minTimeToType(self, word: str) -> int:
        res = 0
        curr = 'a'
        

        alpha = "abcdefghijklmnopqrstuvwxyz"

        for w in word:
            pos1 = alpha.index(w)
            pos2 = alpha.index(curr)
            dis1 = abs(pos1 - pos2)
            dis2 = abs(len(alpha) - dis1)
            disf = min(dis1, dis2) + 1
            res += disf
            curr = w
        return res