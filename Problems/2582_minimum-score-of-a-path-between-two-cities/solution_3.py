class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n+1)]
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        visited = {1}
        queue = collections.deque([1])
        res = float('inf')
        
        while queue:
            u = queue.popleft()

            for v, w in adj[u]:
                res = min(res, w)
                if v not in visited:
                    visited.add(v)
                    queue.append(v)

        return res


