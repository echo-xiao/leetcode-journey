class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        i = 0
        res = 0

        while i < len(cost):
            res += cost[i]
            i += 1
            if i < len(cost):
                res += cost[i]
                i += 1
            i += 1
        return res
        