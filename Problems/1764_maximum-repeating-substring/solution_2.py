class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(sequence)
        m = len(word)
        k = 0

        left = 0 
        right = 0

        while left < n:
            right = left 
            curr = 0

            while right + m <= n:
                if sequence[right: right+m] == word:
                    curr += 1
                    right += m
                else:
                    break
            k = max(k, curr)
            left += 1
        return k