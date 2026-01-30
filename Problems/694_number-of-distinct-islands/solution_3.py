class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ans = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    path = []
                    self.traverse(grid, r, c, path, 'o')
                    ans.add("".join(path))
        return len(ans)


    def traverse(self, grid, r, c, path, dr):
        if (r < 0 or r >= len(grid) or 
            c < 0 or c >= len(grid[0]) or 
            grid[r][c] == 0):
            return

        grid[r][c] = 0
        path.append(dr)
        self.traverse(grid, r, c+1, path, 'r')
        self.traverse(grid, r, c-1, path, 'l')
        self.traverse(grid, r-1, c, path, 'u')
        self.traverse(grid, r+1, c, path, 'd')

        path.append('b')

