class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        cnt = 0

        for i in range(n):
            if not visited[i]:
                cnt += 1
                self.dfs(i, adj, visited)
                
        return cnt
        


    def dfs(self, curr, adj, visited):
        visited[curr] = True
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                self.dfs(neighbor, adj, visited)
            




