class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        indegree = [False] * n
        ans = []

        for u, v in edges:
            indegree[v] = True

        for i in range(n):
            if not indegree[i]:
                ans.append(i)
        
        return ans