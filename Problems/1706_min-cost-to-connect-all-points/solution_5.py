class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [float('inf')] * n
        dist[0] = 0

        visited = [False] * n
        cost = 0

        for _ in range(n):
            u = -1
            for i in range(n):
                if not visited[i] and (u == -1 or dist[i] < dist[u]):
                    u = i
            
            visited[u] = True
            cost += dist[u]

            x, y = points[u]
            for v in range(n):
                if not visited[v]:
                    distance = abs(x - points[v][0]) + abs(y - points[v][1])
                    if distance < dist[v]:
                        dist[v] = distance
        return cost