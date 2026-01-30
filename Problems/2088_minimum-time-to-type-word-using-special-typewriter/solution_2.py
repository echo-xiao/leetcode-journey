class Solution:
    def minTimeToType(self, word: str) -> int:
        res = 0
        curr = 'a'

        for w in word:
            pos1 = ord(curr) - ord('a')
            pos2 = ord(w) - ord('a')
            dis1 = abs(pos1 - pos2)
            dis2 = abs(26 - dis1)
            disf = min(dis1, dis2) + 1
            res += disf
            curr = w
        return res
