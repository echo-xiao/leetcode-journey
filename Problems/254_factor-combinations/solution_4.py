class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        path = []
        self.dfs(n, 2, path, res)
        return res


    def dfs(self, target, start, path, res):
        i = start

        while i * i <= target:
            if target % i == 0:
                res.append(path + [i, target // i])
                self.dfs(target // i, i, path + [i], res)
            i += 1