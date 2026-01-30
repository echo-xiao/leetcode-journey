class Solution:
    def climbStairs(self, n: int) -> int:

        self.dp = [-1] * (n+1)
        return self.climbSteps(n)


    def climbSteps(self, n: int) -> int:
        
        if n == 1:
            return 1
        if n == 2:
            return 2

        if self.dp[n] != -1:
            return self.dp[n]

        step1 = self.climbSteps(n-1)
        step2 = self.climbSteps(n-2)
        self.dp[n] = step1 + step2
        
        return self.dp[n]


