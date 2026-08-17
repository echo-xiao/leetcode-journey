class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        maxres = 0
        fixed = 0
        flex = 0

        for i in range(0, n):
            if grumpy[i] == 0:
                fixed += customers[i]

        for i in range(0, minutes):
            if grumpy[i] == 1:
                flex += customers[i]

        res = fixed + flex
        maxres = res

        for i in range(minutes, n):
            
            if grumpy[i] == 1:
                flex += customers[i]

            if grumpy[i-minutes] == 1:
                flex -= customers[i-minutes]

            res = fixed + flex
            maxres = max(res, maxres)

        return maxres
            