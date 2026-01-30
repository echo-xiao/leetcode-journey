from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        self.mapp = defaultdict(list)

        for u, v in edges:
            self.mapp[u].append(v)
            self.mapp[v].append(u)

        n = len(edges) + 1
        for k, v in self.mapp.items():
            if len(v) == n - 1:
                return k
        return -1
        