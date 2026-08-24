class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minres = 100000
        maxdiff = 0
        for i in range(0, len(prices)):
            minres = min(minres, prices[i])
            diff = prices[i] - minres
            maxdiff = max(maxdiff, diff)
        return maxdiff