from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        
        for cur, pre in prerequisites:
            adj[pre].append(cur) 
            indegrees[cur] += 1  
        
        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
        
        count = 0 
        
    
        while queue:
            u = queue.popleft() 
            count += 1
            
            for v in adj[u]: 
                indegrees[v] -= 1 
                if indegrees[v] == 0: 
                    queue.append(v)   
        
        
        return count == numCourses