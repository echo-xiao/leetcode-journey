class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        self.dfs(n, k, 1, path, res)
        return res


    def dfs(self, n, k, start, path, res):
        if k == len(path):
            res.append(path[:])
            return 

        for num in range(start, n+1):
            path.append(num)
            self.dfs(n, k, num+1, path, res)
            path.pop()
