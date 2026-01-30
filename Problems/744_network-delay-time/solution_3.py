class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:

        # dfs
        
        graph = collections.defaultdict(list)
        for u, v, w in times: graph[u].append((v, w))
        dist = [float('inf')] * (n + 1)
        
        def dfs(node, time):
            if time >= dist[node]: return
            dist[node] = time
            for v, w in sorted(graph[node], key=lambda x: x[1]): # 贪心启发
                dfs(v, time + w)
        
        dfs(k, 0)
        res = max(dist[1:])
        return res if res < float('inf') else -1