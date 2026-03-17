class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for i in range(n-1):
            adj[i].append(i+1)

        res = []
        for u, v in queries:
            adj[u].append(v)

            queue = collections.deque([(0, 0)])
            visited = [False] * n
            visited[0] = True

            while queue:
                curr, depth = queue.popleft()

                if curr == n-1:
                    res.append(depth)
                    break

                for neighbor in adj[curr]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append((neighbor, depth+1))
                
        return res