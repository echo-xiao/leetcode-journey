import collections

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:

        ## dfs

        
        # 1. 构造邻接表并存储为实例变量，方便 dfs 方法访问
        self.graph = collections.defaultdict(list)
        for u, v, w in times:
            self.graph[u].append((v, w))
        
        # 2. 启发式优化：优先走边权小的路径，能更快地更新 dist 从而增加剪枝机会
        for u in self.graph:
            self.graph[u].sort(key=lambda x: x[1])
            
        # 3. 初始化全局最短距离数组
        self.dist = [float('inf')] * (n + 1)
        
        # 4. 调用外部定义的递归函数
        self.dfs(k, 0)
        
        # 5. 计算结果
        max_dist = max(self.dist[1:])
        return max_dist if max_dist != float('inf') else -1

    def dfs(self, node: int, current_time: int):
        """
        独立的 DFS 辅助函数
        :param node: 当前到达的节点
        :param current_time: 从起点到当前节点已花费的时间
        """
        # 关键剪枝：如果当前路径时间已超过或等于已记录的最短时间，直接停止搜索
        if current_time >= self.dist[node]:
            return
        
        # 更新该节点的最短距离记录
        self.dist[node] = current_time
        
        # 递归遍历邻居节点
        if node in self.graph:
            for neighbor, weight in self.graph[node]:
                self.dfs(neighbor, current_time + weight)