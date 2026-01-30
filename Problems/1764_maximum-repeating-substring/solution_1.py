class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        self.sequence = sequence
        self.word = word
        self.n = len(sequence)
        self.m = len(word)

        self.memo = {}

        maxk = 0
        for i in range(self.n):
            maxk = max(maxk, self.recursion(i))

        return maxk


    def recursion(self, i: int) -> int:

        if i < self.m - 1:
            return 0

        if i in self.memo:
            return self.memo[i]

        curr = self.sequence[i - self.m + 1: i + 1]

        if curr == self.word:
            res = 1 + self.recursion(i - self.m)
        else:
            res = 0

        self.memo[i] = res
        return res