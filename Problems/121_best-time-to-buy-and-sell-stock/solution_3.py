class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = self.solve(prices, 0, float('inf'))
        return max(0, res)
        
    def solve(self, prices: List[int], i: int, minPrice: int) -> int:
        if i == len(prices):
            return 0

        profitToday = prices[i] - minPrice

        newMinPrice = min(minPrice, prices[i])
        profitLater = self.solve(prices, i+1, newMinPrice)

        return max(profitToday, profitLater)