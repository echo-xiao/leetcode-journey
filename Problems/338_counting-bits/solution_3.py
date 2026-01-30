class Solution:
    def countBits(self, n: int) -> List[int]:
        
        self.res = []
        for i in range(n+1):
            self.res.append(self.count(i))
        return self.res


    def count(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        val = self.count(n >> 1) + (n & 1)
        return val
        


        