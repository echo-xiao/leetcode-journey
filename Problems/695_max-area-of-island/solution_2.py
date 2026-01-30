class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = self.bfs(grid, r, c)
                    maxArea = max(area, maxArea)
        return maxArea

    def bfs(self, grid, r, c):
        queue = collections.deque([(r, c)])
        cnt = 1
        grid[r][c] = 0

        while queue:
            currR, currC = queue.popleft()

            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nxtR, nxtC = currR + dr, currC + dc

                if (0 <= nxtR < len(grid) and
                    0 <= nxtC < len(grid[0]) and
                    grid[nxtR][nxtC] == 1):
                    queue.append((nxtR, nxtC))
                    grid[nxtR][nxtC] = 0
                    cnt += 1
        return cnt