class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        self.dfs(candidates, target, 0, path, res)
        return res


    def dfs(self, candidates, target, begin, path, res):
        if target == 0:
            res.append(path[:])
            return

        if target < 0:
            return

        for idx in range(begin, len(candidates)):
            c = candidates[idx]

            if idx > begin and candidates[idx] == candidates[idx-1]:
                continue

            path.append(c)
            self.dfs(candidates, target-c, idx+1, path, res)
            path.pop()
            