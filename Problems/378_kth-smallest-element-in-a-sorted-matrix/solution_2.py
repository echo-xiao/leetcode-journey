class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        

        lowVal, highVal = matrix[0][0], matrix[-1][-1]
    

        while lowVal < highVal:
            midVal = lowVal + (highVal - lowVal) // 2
            cnt = self.countLessEqual(matrix, midVal)

            if cnt < k:
                lowVal = midVal + 1
            else:
                highVal = midVal
        return lowVal

    def countLessEqual(self, matrix: List[List[int]], midVal: int) -> int:
        n = len(matrix)
        cnt = 0
        row = n-1
        col = 0

        while row >= 0 and col < n:
            if matrix[row][col] <= midVal:
                cnt += (row+1)
                col += 1
            else:
                row -= 1
        return cnt