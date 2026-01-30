class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = self.dfs(grid, r, c)
                    maxArea = max(area, maxArea)
        return maxArea

    def dfs(self, grid, r, c):
        if (r < 0 or r >= len(grid) or
            c < 0 or c >= len(grid[0]) or 
            grid[r][c] == 0):
            return 0

        grid[r][c] = 0

        return (self.dfs(grid, r, c-1) +
                self.dfs(grid, r, c+1) +
                self.dfs(grid, r+1, c) +
                self.dfs(grid, r-1, c) + 1)
    
        

        

        
