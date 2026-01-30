class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        parent, size, maxArea = self.initialize(grid)

        return self.process(grid, parent, size, maxArea)

    def initialize(self, grid):
        rows, cols = len(grid), len(grid[0])

        parent = [i for i in range(rows * cols)]
        size = [0] * (rows * cols)
        maxArea = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    idx = r * cols + c
                    size[idx] = 1
                    maxArea = max(maxArea, 1)
        return parent, size, maxArea

    def process(self, grid, parent, size, maxArea):
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    idx = r * cols + c

                    if c + 1 < cols and grid[r][c+1] == 1:
                        maxArea = self.union(parent, size, idx, idx+1, maxArea)
                    
                    if r + 1 < rows and grid[r+1][c] == 1:
                        maxArea = self.union(parent, size, idx, idx+cols, maxArea)

        return maxArea

    def find(self, parent, i):
        if parent[i] == i:
            return parent[i]

        parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, size, i, j, maxArea):
        rootI = self.find(parent, i)
        rootJ = self.find(parent, j)

        if rootI != rootJ:
            parent[rootI] = rootJ
            size[rootJ] += size[rootI]

            maxArea = max(maxArea, size[rootJ])

        return maxArea