from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. 初始化入度表和邻接表
        indegrees = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        
        for cur, pre in prerequisites:
            adj[pre].append(cur)  # 先修课指向后续课
            indegrees[cur] += 1   # 后续课的“被依赖数”加 1
        
        # 2. 将所有入度为 0 的课（没有先修课的课）放入队列
        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
        
        count = 0 # 用于记录总共修了多少门课
        
        # 3. 开始“剥洋葱”
        while queue:
            u = queue.popleft() # 修完这门课
            count += 1
            
            for v in adj[u]: # 找到所有依赖这门课的后续课
                indegrees[v] -= 1 # 既然 u 修完了，v 的先修条件就少了一个
                if indegrees[v] == 0: # 如果 v 的所有先修课都修完了
                    queue.append(v)   # v 就可以进队列准备修了
        
        # 4. 如果修完的课等于总课数，说明没有环
        return count == numCourses