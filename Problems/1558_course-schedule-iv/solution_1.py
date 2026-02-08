class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        isPre = [set() for _ in range(numCourses)]

        for u, v in prerequisites:
            adj[u].append(v)
            indegree[v] += 1
            isPre[v].add(u)

        queue = collections.deque([i for i in range(numCourses) if indegree[i] == 0])

        while queue:
            u = queue.popleft()
            for v in adj[u]:
                isPre[v].update(isPre[u])

                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        return [u in isPre[v] for u, v in queries]