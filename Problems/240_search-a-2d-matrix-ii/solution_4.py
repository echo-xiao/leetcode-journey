class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in range(0, len(matrix)):
            left, right = 0, len(matrix[0])-1
            while left <= right:
                col = left + (right - left) // 2
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] < target:
                    left = col + 1
                elif matrix[row][col] > target:
                    right = col - 1
        return False