class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        isPre = [[False] * numCourses for _ in range(numCourses)]

        for u, v in prerequisites:
            isPre[u][v] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if isPre[i][k] and isPre[k][j]:
                        isPre[i][j] = True

        res = []
        for u, v in queries:
            res.append(isPre[u][v])
        return res