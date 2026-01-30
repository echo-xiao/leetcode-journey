class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:

        # Floyd-Warshall ($O(V^3)$)
        
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n): dist[i][i] = 0
        for u, v, w in times: dist[u-1][v-1] = w
        
        for p in range(n): # 中转点
            for i in range(n): # 起点
                for j in range(n): # 终点
                    dist[i][j] = min(dist[i][j], dist[i][p] + dist[p][j])
        
        res = max(dist[k-1])
        return res if res < float('inf') else -1