class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter = self.bfs(grid, r, c)
        return perimeter

    def bfs(self, grid, r, c):
        queue = collections.deque([(r, c)])
        grid[r][c] = 2
        perimeter = 0

        while queue:
            curR, curC = queue.pop()
            perimeter += 4

            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nxtR, nxtC = curR + dr, curC + dc

                if (0 <= nxtR < len(grid) and 0 <= nxtC < len(grid[0])):
                    if grid[nxtR][nxtC] != 0:
                        perimeter -= 1

                    if grid[nxtR][nxtC] == 1:
                        grid[nxtR][nxtC] = 2
                        queue.append((nxtR, nxtC))
        
        return perimeter
            


            