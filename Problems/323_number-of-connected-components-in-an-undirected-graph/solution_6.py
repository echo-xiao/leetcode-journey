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
                queue = collections.deque([i])
                visited[i] = True
                while queue:
                    curr = queue.popleft()
                    for neighbor in adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
        return cnt