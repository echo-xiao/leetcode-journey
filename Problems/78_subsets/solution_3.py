class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        self.dfs(nums, 0, path, res)
        return res


    def dfs(self, nums, start, path, res):

        res.append(path[:])

        if start >= len(nums):
            return 

        for idx in range(start, len(nums)):
            path.append(nums[idx])
            self.dfs(nums, idx+1, path, res)
            path.pop()