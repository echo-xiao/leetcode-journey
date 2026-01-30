class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        return self.dfs(0, adj, visited, n)

    def dfs(self, curr, adj, visited, n):
        if curr in visited:
            return
        
        visited.add(curr)

        for neighbor in adj[curr]:
            self.dfs(neighbor, adj, visited, n)

        return len(visited) == n