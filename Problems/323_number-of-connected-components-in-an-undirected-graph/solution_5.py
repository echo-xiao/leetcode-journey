class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        self.count = n
        
        def find(i):
            if parent[i] == i:
                return i
            # 路径压缩 (Path Compression)：让查找更高效
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j # 将一个根挂在另一个根下
                self.count -= 1
        
        for u, v in edges:
            union(u, v)
            
        return self.count