class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        

        if n <= 8:
            return n
        else:
            if n > 8 and n <= 16:
                return 8 + (n-8) * 2
            else:
                if n > 16 and n <= 24:
                    return 8 + 8 * 2 + (n-16) * 3
                else:
                    return 8 + 8 * 2 + 8 * 3 + (n-24) * 4