from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        
        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        
        stack = []
        for i in range(numCourses):
            if indegree[i] == 0:
                stack.append(i)

        path = [] 
        while stack:
            curr = stack.pop()
            path.append(curr)
            for neighbor in adj[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    stack.append(neighbor)

        if len(path) == numCourses:
            return path
        return []


