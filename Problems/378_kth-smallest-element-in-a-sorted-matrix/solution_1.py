class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        left, right = matrix[0][0], matrix[-1][-1]

        while left < right:
            mid = left + (right - left) // 2
            cnt = self.cntElement(matrix, mid)
            if cnt < k:
                left = mid + 1
            else:
                right = mid
        return left


    def cntElement(self, matrix: List[List[int]], mid: int) -> int:
        row, col = len(matrix)-1, 0
        cnt = 0

        while row >= 0 and col < len(matrix[0]):
            if matrix[row][col] <= mid:
                col += 1
                cnt += (row + 1)
            else:
                row -= 1
        return cnt

        