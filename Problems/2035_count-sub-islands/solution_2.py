class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid2), len(grid2[0])
        cnt = 0

        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1:
                    if self.dfs(grid1, grid2, r, c):
                        cnt += 1

        return cnt

    def dfs(self, grid1, grid2, r, c):
        if (r < 0 or r >= len(grid2) or
            c < 0 or c >= len(grid2[0]) or
            grid2[r][c] == 0):
            return True

        isValid = (grid1[r][c] == 1)

        grid2[r][c] = 0

        right = self.dfs(grid1, grid2, r, c+1)
        left = self.dfs(grid1, grid2, r, c-1)
        up = self.dfs(grid1, grid2, r-1, c)
        down = self.dfs(grid1, grid2, r+1, c)

        return isValid and up and down and left and right
