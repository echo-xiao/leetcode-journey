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
                    self.bfs(grid, r, c)

        return cnt


    def bfs(self, grid, r, c):
        queue = collections.deque([(r, c)])
        grid[r][c] = '0'

        while queue:
            currR, currC = queue.popleft()

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nxtR, nxtC = currR + dr, currC + dc

                if (0 <= nxtR < len(grid) and 
                    0 <= nxtC < len(grid[0]) and
                    grid[nxtR][nxtC] == '1'):

                    queue.append((nxtR, nxtC))
                    grid[nxtR][nxtC] = '0'



                    