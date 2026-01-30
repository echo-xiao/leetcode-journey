class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1, 1]

        lastRow = self.getRow(rowIndex-1)
        newRow = self.newRow(lastRow)
        
        return newRow

    def newRow(self, lastRow: int) -> List[int]:
        newRow = []
        newRow.append(1)
        for idx in range(0, len(lastRow)-1):
            num = lastRow[idx] + lastRow[idx+1]
            newRow.append(num)
        newRow.append(1)
        return newRow

            
            

        

        
        