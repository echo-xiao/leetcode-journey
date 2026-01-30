class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:

        # bfs（spfa变体）
        
        graph = collections.defaultdict(list)
        for u, v, w in times: graph[u].append((v, w))
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        queue = collections.deque([k])
        
        while queue:
            u = queue.popleft()
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    queue.append(v)
        
        res = max(dist[1:])
        return res if res < float('inf') else -1