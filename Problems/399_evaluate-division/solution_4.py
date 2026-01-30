class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)

        for (u, v), val in zip (equations, values):
            graph[u].append((v, val))
            graph[v].append((u, 1.0/val))

        res = []
        for start, end in queries:
            if start not in graph or end not in graph:
                res.append(-1.0)
            else:
                res.append(self.dfs(start, end, set(), graph))

        return res

    def dfs(self, curr, target, visited, graph):
        if curr == target:
            return 1.0

        visited.add(curr)

        for neighbor, weight in graph[curr]:
            if neighbor not in visited:
                res = self.dfs(neighbor, target, visited, graph)
                if res != -1.0:
                    return weight * res

        return -1.0