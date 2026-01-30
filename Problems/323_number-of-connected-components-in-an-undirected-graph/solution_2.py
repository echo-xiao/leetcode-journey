class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        self.parent = [i for i in range(n)]
        self.cnt = n
        
        for u, v in edges:
            self.union(u, v)

        return self.cnt
        

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        rooti = self.find(i)
        rootj = self.find(j)

        if rooti != rootj:
            self.parent[rooti] = rootj
            self.cnt -= 1