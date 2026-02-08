class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[u].append(v)

        isPre = [[False] * numCourses for _ in range(numCourses)] 

        for i in range(numCourses):
            self.dfs(i, i, adj, isPre)
        
        res = []
        for u, v in queries:
            res.append(isPre[u][v])
        return res

    def dfs(self, start, curr, adj, isPre):
        for neighbor in adj[curr]:
            if not isPre[start][neighbor]:
                isPre[start][neighbor] = True
                self.dfs(start, neighbor, adj, isPre)