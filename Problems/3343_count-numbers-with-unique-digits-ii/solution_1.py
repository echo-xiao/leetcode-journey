class Solution:

    def numberCount(self, a: int, b: int) -> int:
        self.s = ""      
        self.L = 0       
        self.memo = {}   

        return self.solve(b) - self.solve(a - 1)

    def solve(self, n: int) -> int:
        
        self.s = str(n)
        self.L = len(self.s)
        self.memo = {}  

        return self.dfs(0, 0, True, True) - 1

    def dfs(self, index: int, mask: int, isTight: bool, isLeadingZero: bool) -> int:

        if index == self.L:
            return 1  

        if not isTight and not isLeadingZero:
            if (index, mask) in self.memo:
                return self.memo[(index, mask)]

        count = 0
        upper_bound = int(self.s[index]) if isTight else 9

        for d in range(upper_bound + 1):
            
            if isLeadingZero and d == 0:
                count += self.dfs(index + 1, mask, isTight and (d == upper_bound), True)
                
            elif (mask & (1 << d)) == 0:
                count += self.dfs(index + 1, mask | (1 << d), isTight and (d == upper_bound), False)


        if not isTight and not isLeadingZero:
            self.memo[(index, mask)] = count
            
        return count