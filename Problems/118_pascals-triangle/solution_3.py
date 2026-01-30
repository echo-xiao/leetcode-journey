class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        return self.recursion(numRows)


    def recursion(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]

        if n == 2:
            return [[1], [1, 1]]

        # 子问题 = 基于最后一行的信息，来获取子问题
        # 最后一行的信息，需要递归公式来解决，n=n-1，然后+子问题

        preProb = self.recursion(n-1)
        subProb = self.subProb(preProb[-1])
        preProb.append(subProb)
        return preProb
         
    
        
    def subProb(self, lastRow: List[int]) -> List[int]:
        newRow = []

        newRow.append(1)
        for idx in range(len(lastRow)-1):
            newRow.append(lastRow[idx]+lastRow[idx+1])
        newRow.append(1)

        return newRow




        