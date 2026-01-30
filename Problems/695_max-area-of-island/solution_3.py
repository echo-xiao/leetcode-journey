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
        stack = [(r, c)]
        cnt = 1
        grid[r][c] = 0

        while stack:
            currR, currC = stack.pop()

            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nxtR, nxtC = currR + dr, currC + dc

                if (0 <= nxtR < len(grid) and
                    0 <= nxtC < len(grid[0]) and
                    grid[nxtR][nxtC] == 1):
                    stack.append((nxtR, nxtC))
                    grid[nxtR][nxtC] = 0
                    cnt += 1
        return cnt