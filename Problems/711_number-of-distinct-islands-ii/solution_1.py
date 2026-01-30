import collections 

class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        ans = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    island = []
                    self.dfs(grid, r, c, visited, island)
                    ans.add(self.getUnique(island))

        return len(ans)

    def dfs(self, grid, r, c, visited, island):
        rows, cols = len(grid), len(grid[0])
        visited.add((r, c))
        island.append((r, c))

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visited:
                self.dfs(grid, nr, nc, visited, island)

    def getUnique(self, shape):
        transforms = []

        for sx, sy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            transforms.append([(x * sx, y * sy) for x, y in shape])
            transforms.append([(y * sx, x * sy) for x, y in shape])

        normalized = []
        for v in transforms:
            v.sort()
            ox, oy = v[0]
            normalized.append(tuple((x - ox, y - oy) for x, y in v))
        
        return min(normalized)