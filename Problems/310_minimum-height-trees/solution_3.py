class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        indegree = [0] * n
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1


        queue = collections.deque()
        for i in range(n):
            if indegree[i] == 1:
                queue.append(i)

        rem = n
        while rem > 2:
            size = len(queue)
            rem -= size

            for _ in range(size):
                curr = queue.popleft()

                for neighbor in adj[curr]:
                    indegree[neighbor] -= 1

                    if indegree[neighbor] == 1:
                        queue.append(neighbor)
        
        return list(queue)