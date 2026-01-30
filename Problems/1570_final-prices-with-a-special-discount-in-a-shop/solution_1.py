class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = list(prices)
        stack = []

        for i, price in enumerate(prices):
            while len(stack) > 0 and prices[stack[-1]] >= price:
                prevIndex = stack.pop()
                res[prevIndex] = prices[prevIndex] - price
            stack.append(i)
        return res