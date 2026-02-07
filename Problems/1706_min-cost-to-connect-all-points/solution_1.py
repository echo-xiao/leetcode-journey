class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parent = list(range(n))
        edges = []

        for i in range(n):
            for j in range(i+1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))

        edges.sort()
        cost = 0
        cnt = 0

        for dist, u, v in edges:
            if self.union(parent, u, v):
                cost += dist
                cnt += 1
                if cnt == n-1:
                    break
        return cost
        

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]


    def union(self, parent, i, j):
        rootI = self.find(parent, i)
        rootJ = self.find(parent, j)

        if rootI != rootJ:
            parent[rootI] = rootJ

            return True
        return False


