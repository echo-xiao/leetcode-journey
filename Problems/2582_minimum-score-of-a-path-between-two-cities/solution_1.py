class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = list(range(n+1))
        min_score = [float('inf')] * (n+1)

        for u, v, w in roads:
            self.union(u, v, w, parent, min_score)

        root1 = self.find(1, parent)
        return min_score[root1]

    def find(self, i, parent):
        if parent[i] == i:
            return i

        parent[i] = self.find(parent[i], parent)
        return parent[i]

    def union(self, i, j, w, parent, min_score):
        root_i = self.find(i, parent)
        root_j = self.find(j, parent)

        curr_min = min(min_score[root_i], min_score[root_j], w)

        if root_i != root_j:
            parent[root_i] = root_j

        min_score[root_j] = curr_min

    