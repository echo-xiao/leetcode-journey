class Solution:
    def fib(self, n: int) -> int:
        
        return self.recursion(n)

    def recursion(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        return self.recursion(n-1) + self.recursion(n-2)