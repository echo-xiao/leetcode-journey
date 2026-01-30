class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        self.dfs(candidates, target, 0, path, res)
        return res


    def dfs(self, candidates, target, begin, path, res):
        if target == 0:
            res.append(path[:])
            return

        if target < 0:
            return 

        for i in range(begin, len(candidates)):
            c = candidates[i]
            path.append(c)
            self.dfs(candidates, target-c, i, path, res)
            path.pop()

