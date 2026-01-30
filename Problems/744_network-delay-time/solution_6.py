import heapq, collections

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:

        # heap 优化djikstra
        
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        pq = [(0, k)] # (距离, 节点)
        dist = {}
        
        while pq:
            d, u = heapq.heappop(pq)
            if u in dist: continue
            dist[u] = d
            for v, w in graph[u]:
                if v not in dist:
                    heapq.heappush(pq, (d + w, v))
                    
        return max(dist.values()) if len(dist) == n else -1