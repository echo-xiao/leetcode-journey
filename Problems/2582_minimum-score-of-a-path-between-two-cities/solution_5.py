class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n+1)]
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))

        self.res = float('inf')
        visited = set()
        self.dfs(1, adj, visited)
        return self.res


    def dfs(self, node, adj, visited):
        if node in visited:
            return

        visited.add(node)

        for v, w in adj[node]:
            if w < self.res:
                self.res = w

            self.dfs(v, adj, visited)
            
