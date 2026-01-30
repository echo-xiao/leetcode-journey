class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        self.dfs(candidates, target, 0, path, res)
        return res


    def dfs(self, candidates, target, start, path, res):
        if target == 0:
            res.append(path[:])
            return 

        if target < 0:
            return 

        for c in range(start, len(candidates)):
            path.append(candidates[c])
            self.dfs(candidates, target-candidates[c], c, path, res)
            path.pop()