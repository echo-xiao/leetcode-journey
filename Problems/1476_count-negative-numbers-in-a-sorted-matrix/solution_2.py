class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(0, len(grid)):
            lst = grid[i]
            left, right = 0, len(lst)-1
            while left <= right:
                mid = left + (right - left) // 2
                if lst[mid] >= 0:
                    left = mid + 1
                elif lst[mid] < 0:
                    right = mid - 1
            length = len(lst[left:])
            res += length
        return res
            
