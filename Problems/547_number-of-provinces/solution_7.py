class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for i in range(len(isConnected)):
            if not visited[i]:
                provinces += 1
                queue = collections.deque([i])
                visited[i] = True

                while queue:
                    curr = queue.popleft()
                    for neighbor in range(n):
                        if isConnected[curr][neighbor] == 1 and not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
        return provinces