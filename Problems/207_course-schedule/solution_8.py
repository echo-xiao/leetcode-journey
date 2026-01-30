class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adj[pre].append(cur)

        flags = [0] * numCourses

        for i in range(numCourses):
            if not self.dfs(i, adj, flags):
                return False
        return True

    def dfs(self, u, adj, flags):
        if flags[u] == 1:
            return False

        if flags[u] == 2:
            return True

        flags[u] = 1

        for v in adj[u]:
            if not self.dfs(v, adj, flags):
                return False

        flags[u] = 2
        return True