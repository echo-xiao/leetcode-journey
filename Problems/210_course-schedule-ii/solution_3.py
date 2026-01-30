from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. 建图并统计入度
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adj[pre].append(cur)
            indegree[cur] += 1
            
        # 2. 将所有入度为 0 的节点入队
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        res = [] # 210 题改用列表存储顺序，而非只计数
        
        # 3. BFS 遍历
        while queue:
            u = queue.popleft()
            res.append(u) # 记录修课顺序
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
                    
        # 4. 判断是否能修完所有课程
        # 如果结果数组长度等于课程总数，返回结果；否则说明有环，返回空数组
        return res if len(res) == numCourses else []