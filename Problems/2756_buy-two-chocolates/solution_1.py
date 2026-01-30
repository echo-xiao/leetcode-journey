class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        ttl = sum(prices[0:2])
        if ttl > money:
            return money
        else:
            return money - ttl
