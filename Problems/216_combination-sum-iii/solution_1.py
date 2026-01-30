class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        self.dfs(k, n, 1, path, res)
        return res

    def dfs(self, k, n, start, path, res):
        if len(path) == k and sum(path) == n:
            res.append(path[:])
            return

        for num in range(start, 10):
            if sum(path) + num > n:
                break
            
            path.append(num)
            self.dfs(k, n, num+1, path, res)
            path.pop()
