class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])

        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        pq = [(0, 0, 0)]

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while pq:
            d, r, c = heapq.heappop(pq)

            if r == n-1 and c == m-1:
                return d

            if d > dist[r][c]:
                continue

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < m:
                    newTime = max(d, moveTime[nr][nc]) + 1

                    if newTime < dist[nr][nc]:
                        dist[nr][nc] = newTime
                        heapq.heappush(pq, (newTime, nr, nc))

        return -1
        