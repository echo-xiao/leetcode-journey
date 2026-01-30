from typing import List, Tuple, Dict

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        self.words = words
        self.groups = groups
        self.N = len(words)
        self.memo = {}
        
        if not words:
            return []
        
        return self.solve(0, -1)


    def solve(self, i: int, prev: int) -> List[str]:

        if i == self.N:
            return []

        if (i, prev) in self.memo:
            return self.memo[(i, prev)]

        ifDropped = self.solve(i + 1, prev)
        maxRes = ifDropped

        curr = self.groups[i]
        
        if curr != prev:
            afterChoosen = self.solve(i + 1, curr)
            ifChoosen = [self.words[i]] + afterChoosen
            if len(ifChoosen) > len(maxRes):
                maxRes = ifChoosen

        self.memo[(i, prev)] = maxRes
        return maxRes

    
