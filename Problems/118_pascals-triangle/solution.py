class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        arr = [[1]]

        for i in range(1, numRows):
            lastRow = arr[-1]
            newRow = [1]
            for j in range(len(lastRow)-1):
                newRow.append(lastRow[j]+lastRow[j+1])
            newRow.append(1)
            arr.append(newRow)
            
        return arr