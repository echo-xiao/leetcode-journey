class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        ans = set()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    shape = self.traverse(grid, r, c)
                    ans.add(shape)
        return len(ans)


    def traverse(self, grid, sr, sc):
        rows, cols = len(grid), len(grid[0])
        stack = [(sr, sc)]
        grid[sr][sc] = 0

        currIsland = []

        while stack:
            cr, cc = stack.pop()
            currIsland.append((cr - sr, cc - sc))

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = cr + dr, cc + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 0
                    stack.append((nr, nc))

        return tuple(sorted(currIsland))