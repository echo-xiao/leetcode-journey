class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        cnt = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    self.dfs(grid, r, c)
                    cnt += 1

        return cnt

    def dfs(self, grid, r, c):
        if (r < 0 or r >= len(grid) or 
            c < 0 or c >= len(grid[0]) or
            grid[r][c] == '0'):
           return 

        grid[r][c] = '0'

        self.dfs(grid, r, c+1)
        self.dfs(grid, r, c-1)
        self.dfs(grid, r-1, c)
        self.dfs(grid, r+1, c)

