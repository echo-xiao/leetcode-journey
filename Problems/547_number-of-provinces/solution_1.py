class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = list(range(n))
        cnt = n

        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    if self.union(i, j, parent):
                        cnt -= 1
        return cnt

        
    def find(self, i, parent):
        if parent[i] == i:
            return i

        parent[i] = self.find(parent[i], parent)
        return parent[i]

    def union(self, i, j, parent):
        rootI, rootJ = self.find(i, parent), self.find(j, parent)

        if rootI != rootJ:
            parent[rootI] = rootJ
            return True
        return False

