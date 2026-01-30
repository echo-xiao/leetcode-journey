class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 2:
            return [i for i in range(n)]

        sys.setrecursionlimit(30000)

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        pathA = self.getLongestPath(0, -1, adj)
        nodeA = pathA[-1]

        pathB = self.getLongestPath(nodeA, -1, adj)

        pathLen = len(pathB)
        mid = pathLen // 2

        if pathLen % 2 == 1:
            return [pathB[mid]]
        else:
            return [pathB[mid-1], pathB[mid]]

        
    def getLongestPath(self, curr, parent, adj) -> List[int]:
        maxSubPath = []

        for neighbor in adj[curr]:
            if neighbor != parent:
                subPath = self.getLongestPath(neighbor, curr, adj)
                if len(subPath) > len(maxSubPath):
                    maxSubPath = subPath

        return [curr] + maxSubPath
