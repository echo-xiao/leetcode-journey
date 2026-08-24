class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice = float('inf')
        maxProfit = 0

        for i in range(0, len(prices)):

            minPrice = min(minPrice, prices[i])
            maxProfit = max(maxProfit, prices[i]-minPrice)

        return maxProfit