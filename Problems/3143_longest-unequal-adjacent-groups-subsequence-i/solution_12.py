class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        if not words:
            return []

        start0 = self.build(words, groups, 0)
        start1 = self.build(words, groups, 1)
        
        if len(start0) >= len(start1):
            return start0
        else:
            return start1       


    def build(self, words: List[str], groups: List[int], start: int) -> List[str]:

        N = len(words)
        res = []

        expected = start
        
        for i in range(N):
            current = groups[i]
            
            if current == expected:
                res.append(words[i])
                
                expected = 1 - expected
                
        return res


