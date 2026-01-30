class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        m = len(matrix)
        n = len(matrix[0])

        left, right = 0, m*n-1


        while left <= right:
            mid = left + (right - left) // 2

            row = mid // n
            col = mid % n
            midVal = matrix[row][col]

            if midVal == target:
                return True
            elif midVal > target:
                right = mid - 1
            else:
                left = mid + 1
        return False