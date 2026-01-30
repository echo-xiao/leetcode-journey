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

                stack = [i]
                while stack:
                    curr = stack.pop()

                    if not visited[curr]:
                        visited[curr] = True
                        for neighbor in adj[curr]:
                            if not visited[neighbor]:
                                stack.append(neighbor)

        return cnt
