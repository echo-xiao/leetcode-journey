class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adj[pre].append(cur)
        
        # 0: 未访问, 1: 正在访问, 2: 已完成
        visited = [0] * numCourses
        res = []
        
        for i in range(numCourses):
            if visited[i] != 0:
                continue
            
            # 栈中存储形式：(node, state)
            # state 为 0 表示第一次遇到（准备遍历邻居）
            # state 为 1 表示邻居已压栈（准备回溯归档）
            stack = [(i, 0)]
            
            while stack:
                u, state = stack.pop()
                
                if state == 0:
                    if visited[u] == 1: return [] # 发现环
                    if visited[u] == 2: continue # 已处理过
                    
                    visited[u] = 1 # 标记为正在访问
                    # 再次压入自己，但状态改为 1，表示接下来该归档了
                    stack.append((u, 1))
                    
                    # 将邻居压栈（准备深入探测）
                    for v in adj[u]:
                        if visited[v] == 0:
                            stack.append((v, 0))
                        elif visited[v] == 1:
                            return [] # 发现环
                else:
                    # 此时 state == 1，说明该节点的邻居都已探测完毕
                    if visited[u] != 2:
                        visited[u] = 2
                        res.append(u)
                        
        return res[::-1] if len(res) == numCourses else []