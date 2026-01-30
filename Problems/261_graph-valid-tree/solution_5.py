class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        return self.dfs(0, adj, visited)

    def dfs(self, curr, adj, visited):
        
        visited[curr] = True

        for neighbor in adj[curr]:
            if not visited[neighbor]:
                self.dfs(neighbor, adj, visited)

        return all(visited)