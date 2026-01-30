class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 1. 初始化状态：作为局部变量或实例变量
        self.parent = list(range(n))
        self.count = n
        
        # 2. 遍历每一条边进行合并
        for u, v in edges:
            self.union(u, v)
            
        return self.count

    # 辅助方法 1：找老大
    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        # 路径压缩
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    # 辅助方法 2：合并
    def union(self, i: int, j: int):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.count -= 1