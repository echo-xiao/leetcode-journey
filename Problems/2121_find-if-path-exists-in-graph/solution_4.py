from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # 遍历列表，构建一个字典，字典里面是每个点，以及他的领居
        # 构建一张visit表，如果visit过了，就放进去
        # 从source开始visit
        # 遍历一遍列表，找每个点，以及对应的领居


        self.mapp = defaultdict(list)
        for u, v in edges:
            self.mapp[u].append(v)
            self.mapp[v].append(u)
        
        self.visited = set()
        self.destination = destination
        
        return self.dfs(source)

    def dfs(self, curr: int):
        if curr == self.destination:
            return True

        if curr in self.visited:
            return False

        self.visited.add(curr)

        for i in self.mapp[curr]:
            if self.dfs(i):
                return True

        return False



