class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        self.parent = list(range(m * n))
        self.isLand =[False] * (m * n)
        self.cnt = 0

        res = []

        for r, c in positions:
            idx = r * n + c
            if self.isLand[idx]:
                res.append(self.cnt)
                continue

            self.isLand[idx] = True
            self.cnt += 1

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                nidx = nr * n + nc
                if 0 <= nr < m and 0 <= nc < n and self.isLand[nidx]:
                    self.union(idx, nidx)

            res.append(self.cnt)
        return res

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        rooti = self.find(i)
        rootj = self.find(j)
        if rooti != rootj:
            self.parent[rooti] = rootj
            self.cnt -= 1




























