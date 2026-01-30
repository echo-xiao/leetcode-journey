class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1], [1, 1]]

        preProb = self.generate(numRows-1)
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




        