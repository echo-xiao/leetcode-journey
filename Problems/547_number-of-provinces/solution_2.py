class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
         
        n = len(isConnected)
        provinces = 0
        visited = set()

        for i in range(n):
            if i not in visited:
                provinces += 1
                self.traverse(i, isConnected, visited, n)

        return provinces

    def traverse(self, i, isConnected, visited, n):
        stack = [i]

        while stack:
            curr = stack.pop()

            if curr not in visited:
                visited.add(curr)
                for j in range(n):
                    if isConnected[curr][j] == 1 and j not in visited:
                        stack.append(j)