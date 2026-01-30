class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        self.dfs(nums, 0, res, path)
        return res


    def dfs(self, nums, start, res, path):

        res.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            self.dfs(nums, i+1, res, path)
            path.pop()

