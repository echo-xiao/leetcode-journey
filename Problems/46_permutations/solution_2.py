class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        self.dfs(nums, path, res)
        return res

    def dfs(self, nums, path, res):

        if len(nums) == len(path):
            res.append(path[:])
            return 

        for n in nums:

            if n in path:
                continue

            path.append(n)
            self.dfs(nums, path, res)
            path.pop()


