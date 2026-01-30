class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        boundary = []
        cnt = 0

        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows-1 or c == 0 or c == cols-1:
                    if grid[r][c] == 0:
                        boundary.append((r, c))

        while boundary:
            currR, currC = boundary.pop()
            self.dfs(grid, currR, currC)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    cnt += 1
                    self.dfs(grid, r, c)

        return cnt


    def dfs(self, grid, r, c):
        if (r < 0 or r >= len(grid) or
            c < 0 or c >= len(grid[0]) or 
            grid[r][c] == 1):
            return 

        grid[r][c] = 1

        self.dfs(grid, r, c+1)
        self.dfs(grid, r, c-1)
        self.dfs(grid, r+1, c)
        self.dfs(grid, r-1, c)