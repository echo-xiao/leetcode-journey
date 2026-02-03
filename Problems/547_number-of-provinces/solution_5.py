class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
         
        n = len(isConnected)
        provinces = 0
        visited = set()

        for i in range(n):
            if i not in visited:
                provinces += 1
                visited.add(i)
                self.traverse(i, isConnected, visited, n)

        return provinces

    def traverse(self, i, isConnected, visited, n):
        queue = collections.deque([i])

        while queue:
            curr = queue.popleft()
            for j in range(n):
                if isConnected[curr][j] == 1 and j  not in visited:
                    visited.add(j)
                    queue.append(j)