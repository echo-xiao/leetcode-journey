class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        self.dfs(n, k, path, res)
        return res


    def dfs(self, n, k, path, res):
        if k == len(path):
            res.append(path[:])
            return 

        for num in range(n, k-len(path)-1, -1):
            path.append(num)
            self.dfs(num-1, k, path, res)
            path.pop()
