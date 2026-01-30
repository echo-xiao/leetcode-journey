class Solution:
    def fib(self, n: int) -> int:
        self.dp = [-1] * (n+1)
        return self.recursion(n)

    def recursion(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
            
        if self.dp[n] != -1:
            return self.dp[n]

        self.dp[n] = self.recursion(n-1) + self.recursion(n-2)
        
        return self.dp[n]