from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # 把现有的list改成，node和neighbors的形式
        # 有一个visited的set，用来判断这些node是否已经visit过
        # 调用dfs(source)开始遍历

        # 如果找到了destination，返回true
        # 如果发现已经visited过了，返回false
        # 如果没有visit过，假如到visited里面去
        # 遍历整个多叉树的邻居们，如果找到了就返回true
        # 如果还没有，就返回false


        self.mapp = defaultdict(list)
        for u, v in edges:
            self.mapp[u].append(v)
            self.mapp[v].append(u)
        
        self.visited = [False] * n
        self.destination = destination
        self.found = False

        self.traverse(source)
        return self.found

    def traverse(self, idx: int):
        if self.found:
            return

        if self.visited[idx]:
            return 

        self.visited[idx] = True

        if idx == self.destination:
            self.found = True
            return 

        for neighbor in self.mapp[idx]:
            self.traverse(neighbor)


