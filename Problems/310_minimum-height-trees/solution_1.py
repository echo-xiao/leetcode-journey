import collections

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        # 1. 基础边界情况
        if n <= 2:
            return [i for i in range(n)]
        
        # 2. 构建邻接表
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # 3. 第一次迭代 DFS：从 0 出发找到一个端点 node_A
        node_A, _ = self._get_farthest_node_and_path(0, n, adj)
        
        # 4. 第二次迭代 DFS：从 node_A 出发找到另一个端点 node_B，并拿回父节点映射
        node_B, parent_map = self._get_farthest_node_and_path(node_A, n, adj)
        
        # 5. 根据 parent_map 从 node_B 回溯到 node_A，重建直径路径
        path = []
        curr = node_B
        while curr != -1:
            path.append(curr)
            curr = parent_map[curr]
            
        # 6. 取路径中点
        path_len = len(path)
        mid = path_len // 2
        if path_len % 2 == 1:
            return [path[mid]]
        else:
            return [path[mid - 1], path[mid]]

    def _get_farthest_node_and_path(self, start_node: int, n: int, adj: list[list[int]]):
        """
        使用 Stack 的迭代 DFS。
        返回: (最远节点, 用于回溯路径的 parent 字典)
        """
        # stack 存储: (当前节点, 父节点, 当前深度)
        stack = [(start_node, -1, 0)]
        parent_map = {start_node: -1}
        
        farthest_node = start_node
        max_dist = 0
        
        # 记录已访问节点，防止在无向图中死循环
        visited = {start_node}
        
        while stack:
            u, p, dist = stack.pop()
            
            # 更新最远距离和对应的节点
            if dist > max_dist:
                max_dist = dist
                farthest_node = u
            
            for v in adj[u]:
                if v not in visited:
                    visited.add(v)
                    parent_map[v] = u # 记录路径
                    stack.append((v, u, dist + 1))
                    
        return farthest_node, parent_map