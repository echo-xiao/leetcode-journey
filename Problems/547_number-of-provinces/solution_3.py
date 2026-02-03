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
        visited.add(i)

        for j in range(n):
            if isConnected[i][j] == 1 and j not in visited:
                self.traverse(j, isConnected, visited, n)