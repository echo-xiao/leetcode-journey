class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        cnt = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    cnt += 1
                    self.dfs(grid, r, c)

        return cnt


    def dfs(self, grid, r, c):
        stack = [(r, c)]
        grid[r][c] = '0'

        while stack:
            currR, currC = stack.pop()

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nxtR, nxtC = currR + dr, currC + dc

                if (0 <= nxtR < len(grid) and 
                    0 <= nxtC < len(grid[0]) and
                    grid[nxtR][nxtC] == '1'):

                    stack.append((nxtR, nxtC))
                    grid[nxtR][nxtC] = '0'



                    