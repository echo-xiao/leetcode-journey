class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        ttl = 0
        cost = 1

        while n > 0:
            slot = min(n, 8)
            ttl += slot * cost
            n -= slot
            cost += 1
        return ttl