class Solution:
    def countBits(self, n: int) -> List[int]:
        
        self.res = [-1] * (n+1)
        for i in range(n+1):
            self.res[i] = self.count(i)
        return self.res


    def count(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        if self.res[n] != -1:
            return self.res[n]

        self.res[n] = self.count(n // 2) + (n % 2)
        return self.res[n]
        


        