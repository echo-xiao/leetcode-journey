class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        n1 = len(word1)
        n2 = len(word2)

        n = max(n1, n2)

        merged = []

        for i in range(0, n):
            if i < n1:
                merged.append(word1[i])
            if i < n2:
                merged.append(word2[i])


        
        return "".join(merged)