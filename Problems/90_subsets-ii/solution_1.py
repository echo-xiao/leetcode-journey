class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums.sort()

        self.dfs(nums, 0, path, res)
        return res

    def dfs(self, nums, idx, path, res):

        res.append(path[:])

        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            self.dfs(nums, i+1, path, res)
            path.pop()