class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ans = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    path = []
                    stack = [(r, c)]
                    grid[r][c] = 0

                    while stack:
                        cr, cc = stack.pop()
                        path.append((cr - r, cc - c))

                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = cr + dr, cc + dc

                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                                grid[nr][nc] = 0 
                                stack.append((nr, nc))

                    path.sort()
                    ans.add(tuple(path))

        return len(ans)
                        