import collections

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:

        ## dfs

        self.graph = collections.defaultdict(list)
        for u, v, w in times:
            self.graph[u].append((v, w))
        
        for u in self.graph:
            self.graph[u].sort(key=lambda x: x[1])
            
        self.dist = [float('inf')] * (n + 1)
        
        self.dfs(k, 0)
        
        max_dist = max(self.dist[1:])
        return max_dist if max_dist != float('inf') else -1

    def dfs(self, node: int, current_time: int):

        if current_time >= self.dist[node]:
            return
        
        self.dist[node] = current_time
        
        if node in self.graph:
            for neighbor, weight in self.graph[node]:
                self.dfs(neighbor, current_time + weight)