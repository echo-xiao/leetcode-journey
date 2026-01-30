class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)

        for (u, v), value in zip(equations, values):
            graph[u].append((v, value))
            graph[v].append((u, 1.0/value))

        res = []
        for start, end in queries:
            if start not in graph or end not in graph:
                res.append(-1.0)
                continue
            
            found = False
            stack = [(start, 1.0)]
            visited = set()

            while stack:
                curr, currProduct = stack.pop()

                if curr == end:
                    res.append(currProduct)
                    found = True
                    break

                visited.add(curr)

                for neighbor, weight in graph[curr]:
                    if neighbor not in visited:
                        stack.append((neighbor, currProduct * weight))
            if not found:
                res.append(-1.0)

        return res