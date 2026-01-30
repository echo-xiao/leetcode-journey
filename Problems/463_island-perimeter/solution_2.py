class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter = self.dfs(grid, r, c)
        return perimeter

    def dfs(self, grid, r, c):
        stack = [(r, c)]
        grid[r][c] = 2
        perimeter = 0

        while stack:
            curR, curC = stack.pop()
            perimeter += 4

            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nxtR, nxtC = curR + dr, curC + dc

                if (0 <= nxtR < len(grid) and 0 <= nxtC < len(grid[0])):
                    if grid[nxtR][nxtC] != 0:
                        perimeter -= 1
                        
                    if grid[nxtR][nxtC] == 1:
                        grid[nxtR][nxtC] = 2
                        stack.append((nxtR, nxtC))
        
        return perimeter
            


            