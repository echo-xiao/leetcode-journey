class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(0, len(grid)):
            lst = grid[i]
            left = self.helper(lst, 0, len(lst)-1)
            length = len(lst[left:])
            res += length
        return res
        
    def helper(self, lst: List[int], left: int, right = int) -> int:
        if left > right:
            return left

        mid = left + (right - left) // 2
        if lst[mid] >= 0:
            return self.helper(lst, mid+1, right)
        else:
            return self.helper(lst, left, mid-1)
        
            
