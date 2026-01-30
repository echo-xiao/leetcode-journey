from collections import deque
from typing import List  # 如果 Python 版本 < 3.9，需要这个

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        
        # 1. 建图并统计入度
        for cur, pre in prerequisites:
            adj[pre].append(cur)
            indegree[cur] += 1
            
        # 2. 将所有入度为 0 的节点入队
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        visited_count = 0
        
        # 3. BFS
        while queue:
            u = queue.popleft()
            visited_count += 1
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
                    
        # 4. 如果访问过的节点数等于总数，说明无环
        return visited_count == numCourses