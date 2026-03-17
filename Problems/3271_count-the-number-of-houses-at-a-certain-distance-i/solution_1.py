class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        dist = [[float('inf')] * (n + 1) for _ in range(n+1)]
        for i in range(1, n+1):
            dist[i][i] = 0

        for i in range(1, n):
            dist[i][i+1] = dist[i+1][i] = 1

        if x != y:
            dist[x][y] = dist[y][x] = 1

        for k in range(1, n+1):
            for i in range(1, n+1):
                for j in range(1, n+1):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        res = [0] * n
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i != j:
                    d = dist[i][j]
                    res[d-1] += 1
            
        return res