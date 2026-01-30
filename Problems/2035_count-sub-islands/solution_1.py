class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid2), len(grid2[0])
        cnt = 0

        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1:
                    if self.floor(grid1, grid2, r, c):
                        cnt += 1

        return cnt

    def floor(self, grid1, grid2, r, c):
        rows, cols = len(grid2), len(grid2[0])
        stack = [(r, c)]
        grid2[r][c] = 0

        isSub = True
        while stack:
            cr, cc = stack.pop()

            if grid1[cr][cc] == 0:
                isSub = False

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = cr + dr, cc + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid2[nr][nc] == 1:
                    grid2[nr][nc] = 0
                    stack.append((nr, nc))

        return isSub