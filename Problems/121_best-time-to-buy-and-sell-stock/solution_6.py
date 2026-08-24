class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice = float('inf')
        maxProfit = -1
        for idx in range(0, len(prices)):
            minPrice = min(minPrice, prices[idx])
            maxProfit = max((prices[idx] - minPrice), maxProfit)

        return maxProfit
            