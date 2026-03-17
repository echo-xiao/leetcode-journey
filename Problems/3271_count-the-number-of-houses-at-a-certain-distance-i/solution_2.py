class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        adj = [[] for _ in range(n+1)]
        for i in range(1, n):
            adj[i].append(i+1)
            adj[i+1].append(i)
        adj[x].append(y)
        adj[y].append(x)

        res = [0] * n

        for j in range(1, n+1):
            queue = collections.deque([(j, 0)])
            visited = {j}
            
            while queue:
                curr, dist = queue.popleft()
                if dist > 0:
                    res[dist-1] += 1
                
                for v in adj[curr]:
                    if v not in visited:
                        visited.add(v)
                        queue.append((v, dist+1))
        return res