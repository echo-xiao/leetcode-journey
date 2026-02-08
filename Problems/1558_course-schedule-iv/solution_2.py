class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[u].append(v)

        memo = [[-1] * numCourses for _ in range(numCourses)]

        res = []
        for u, v in queries:
            if self.canReach(u, v, adj, memo):
                res.append(True)
            else:
                res.append(False)
        return res

    def canReach(self, u, v, adj, memo):
        if memo[u][v] != -1:
            return memo[u][v] == 1
        
        for neighbor in adj[u]:
            if neighbor == v or self.canReach(neighbor, v, adj, memo):
                memo[u][v] = 1
                return True

        memo[u][v] = 0
        return False
