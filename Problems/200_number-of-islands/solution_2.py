class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        parent, cnt = self.initialize(grid)

        finalCnt = self.process(grid, parent, cnt)

        return finalCnt

    def initialize(self, grid):
        rows, cols = len(grid), len(grid[0])
        parent = [-1] * (rows * cols)
        cnt = 0

        for r in range(rows):
            for c in range(cols):
                idx = r * cols + c
                parent[idx] = idx
                if grid[r][c] == '1':
                    cnt += 1
        return parent, cnt

    def process(self, grid, parent, cnt):
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    currIdx = r * cols + c

                    if c+1 < cols and grid[r][c+1] == '1':
                        if self.union(parent, currIdx, currIdx+1):
                            cnt -= 1

                    if r+1 < rows and grid[r+1][c] == '1':
                        if self.union(parent, currIdx, currIdx+cols):
                            cnt -= 1
        return cnt


    def find(self, parent, i):
        if parent[i] == i:
            return i

        parent[i] = self.find(parent, parent[i])
        return parent[i]


    def union(self, parent, i, j):
        rootI = self.find(parent, parent[i])
        rootJ = self.find(parent, parent[j])

        if rootI != rootJ:
            parent[rootI] = rootJ
            return True

        return False