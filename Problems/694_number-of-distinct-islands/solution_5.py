class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ans = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    path = []
                    self.dfs(grid, r, c, path, 'o')
                    ans.add("".join(path))
        return len(ans)
                    

    def dfs(self, grid, r, c, path, direction):
        rows, cols = len(grid), len(grid[0])

        if (r < 0 or r >= rows or
            c < 0 or c >= cols or 
            grid[r][c] == 0):
            return

        path.append(direction)
        grid[r][c] = 0

        self.dfs(grid, r, c+1, path, 'right')
        self.dfs(grid, r, c-1, path, 'left')
        self.dfs(grid, r+1, c, path, 'down')
        self.dfs(grid, r-1, c, path, 'up')

        path.append("b")