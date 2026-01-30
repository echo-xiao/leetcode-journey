class Solution:
    def divisorGame(self, n: int) -> bool:

        self.memo = {}        
        return self.canWin(n)

    def canWin(self, k: int) -> bool:

        
        if k == 1:
            return False
        
        if k in self.memo:
            return self.memo[k]
        

        for x in range(1, k // 2 + 1):
            if k % x == 0:
                if not self.canWin(k - x):
                    self.memo[k] = True 
                    return True
        
        self.memo[k] = False 
        return False