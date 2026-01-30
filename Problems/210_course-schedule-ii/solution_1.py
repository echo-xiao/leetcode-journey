from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[v].append(u)

        states = [0] * numCourses
        res = []

        for i in range(numCourses):
            if states[i] == 0:
                if not self.dfs(i, adj, states, res):
                    return []
        return res[::-1]


    def dfs(self, u, adj, states, res):
        if states[u] == 2: return True
        if states[u] == 1: return False

        states[u] = 1

        for neighbor in adj[u]:
            if not self.dfs(neighbor, adj, states, res):
                return False

        states[u] = 2
        res.append(u)
        return True