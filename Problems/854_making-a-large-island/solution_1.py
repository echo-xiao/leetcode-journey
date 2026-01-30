class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        area = {0:0}
        islandid = 2

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    size = self.getArea(grid, r, c, islandid)
                    area[islandid] = size
                    islandid += 1

        maxArea = max(area.values() or [0])

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seenIsland = set()

                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1,0)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            seenIsland.add(grid[nr][nc])
                        currComb = 1 + sum(area[idx] for idx in seenIsland)
                        maxArea = max(maxArea, currComb)

        return maxArea

    def getArea(self, grid: List[List[int]], r: int, c: int, idx: int):
        n = len(grid)
        size = 0 
        stack = [(r, c)]
        grid[r][c] = idx

        while stack:
            currR, currC = stack.pop()
            size += 1
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = currR + dr, currC + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = idx
                    stack.append((nr, nc))
        return size































