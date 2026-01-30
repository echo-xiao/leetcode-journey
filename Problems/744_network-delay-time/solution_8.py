class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[float('inf')] * n for _ in range(n)]
        for u, v, w in times:
            graph[u-1][v-1] = min(graph[u-1][v-1], w)

        dist = [float('inf')]  * n
        dist[k-1] = 0
        visited = [False] * n

        for _ in range(n):
            x = -1
            for y in range(n):
                if not visited[y] and (x == -1 or dist[y] < dist[x]):
                    x = y

            if dist[x] == float('inf'):
                break

            visited[x] = True

            for y in range(n):
                if graph[x][y] != float('inf'):
                    dist[y] = min(dist[y], dist[x] + graph[x][y])

        maxDist = max(dist)
        if maxDist < float('inf'):
            return int(maxDist)
        else:
            return -1
