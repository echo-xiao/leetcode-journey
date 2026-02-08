class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            graph[u].append(v)

        isPre = [[False] * numCourses for _ in range(numCourses)]

        for i in range(numCourses):
            self.dfs(i, i, graph, isPre)

        res = []
        for u, v in queries:
            res.append(isPre[u][v])
        return res


    def dfs(self, start, curr, graph, isPre):
        for neighbor in graph[curr]:
            if not isPre[start][neighbor]:
                isPre[start][neighbor] = True
                self.dfs(start, neighbor, graph, isPre)
        