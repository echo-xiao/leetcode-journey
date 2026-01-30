class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adj[cur].append(pre)

        flag = [0] * numCourses
        stack = []

        for i in range(numCourses):
            if flag[i] != 0:
                continue

            stack = [i]
            while stack:
                u = stack[-1]
                if flag[u] == 0:
                    flag[u] = 1
                    for v in adj[u]:
                        if flag[v] == 1:
                            return False
                        if flag[v] == 0:
                            stack.append(v)
                else:
                    if flag[u] == 1:
                        flag[u] = 2
                    stack.pop()
        return True
