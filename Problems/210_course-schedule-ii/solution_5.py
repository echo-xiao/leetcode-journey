class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adj[pre].append(cur)

        flags = [0] * numCourses
        res = []

        for i in range(numCourses):
            if not self.dfs(i, adj, flags, res):
                return []

        return res[::-1]

    def dfs(self, u, adj, flags, res):
        if flags[u] == 1:
            return False

        if flags[u] == 2:
            return True

        flags[u] = 1
        for v in adj[u]:
            if not self.dfs(v, adj, flags, res):
                return False

        flags[u] = 2
        res.append(u)
        return True