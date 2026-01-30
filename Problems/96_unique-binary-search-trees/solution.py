class Solution:
        
    def numTrees(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)

    def helper(self, n: int, memo: dict) -> int:
        if n in memo:
            return memo[n]

        if n <= 1:
            return 1

        res = 0
        for i in range(1, n+1):
            leftSide = self.helper(i-1, memo)
            rightSide = self.helper(n-i, memo)
            res += leftSide * rightSide

        memo[n] = res
        return res