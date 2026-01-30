class Solution:
    def __init__(self):
        self.parent = {}
        self.weight = {}


    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.parent = {}
        self.parent = {}

        for (u, v), val in zip(equations, values):
            self.union(u, v, val)

        res = []
        for u, v in queries:
            if u not in self.parent or v not in self.parent:
                res.append(-1.0)
            else:
                rootU = self.find(u)
                rootV = self.find(v)
                if rootU != rootV:
                    res.append(-1.0)
                else:
                    res.append(self.weight[u] / self.weight[v])

        return res


    def find(self, i):
        if i not in self.parent:
            self.parent[i] = i
            self.weight[i] = 1.0
            return i

        if self.parent[i] == i:
            return i

        oldParent = self.parent[i]
        root = self.find(oldParent)

        self.parent[i] = root

        self.weight[i] *= self.weight[oldParent]

        return root

    def union(self, i, j, value):
        rooti = self.find(i)
        rootj = self.find(j)

        if rooti != rootj:
            self.parent[rooti] = rootj
            self.weight[rooti] = value * self.weight[j] / self.weight[i]


        



