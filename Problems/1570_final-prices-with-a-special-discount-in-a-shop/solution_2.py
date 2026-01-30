class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = list(prices)
        stack = []

        for i in range(len(prices)-1, -1, -1):
            while len(stack) > 0 and stack[-1] > prices[i]:
                    stack.pop()
                    
            if len(stack) == 0:
                pass
            else:
                discount = stack[-1]
                res[i] = prices[i] - discount

            stack.append(prices[i])
        return res
