class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        minHeap = [(0, 0)]
        cost = 0


        while minHeap:
            dist, u = heapq.heappop(minHeap)

            if visited[u]:
                continue
            
            visited[u] = True
            cost += dist

            x, y = points[u]
            for v in range(n):
                if not visited[v]:
                    newDist = abs(x - points[v][0]) + abs(y - points[v][1])
                    heapq.heappush(minHeap, (newDist, v))
        
        return cost