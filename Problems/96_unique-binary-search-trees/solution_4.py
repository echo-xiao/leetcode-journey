class Solution:
    @cache
    
    def numTrees(self, n: int) -> int:
        
        if n <= 1:
            return 1
        res = 0
        for i in range(1, n+1):
            leftSide = self.numTrees(i-1)
            rightSide = self.numTrees(n-i)
            res += leftSide * rightSide
    
        return res