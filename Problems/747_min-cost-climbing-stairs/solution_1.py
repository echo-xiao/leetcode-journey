class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        self.cost = cost
        self.n = len(cost)
        self.dp = [-1] * (self.n + 1)

        return min(self.recursion(self.n - 1), self.recursion(self.n - 2)) 


    def recursion(self, n: int) -> int:
        if n == 0:
            return self.cost[0]
        
        if n == 1:
            return self.cost[1]

        if self.dp[n] != -1:
            return self.dp[n]

        self.dp[n] = min(self.recursion(n-1), self.recursion(n-2)) + self.cost[n]
        return self.dp[n]
        
        