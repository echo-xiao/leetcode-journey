class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)
        self.dfs(nums, used, path, res)
        return res

    def dfs(self, nums, used, path, res):


        if len(nums) == len(path):
            res.append(path[:])
            return 
        


        for i in range(len(nums)):

            if used[i] == True:
                continue

            path.append(nums[i])
            used[i] = True

            self.dfs(nums, used, path, res)
            
            path.pop()
            used[i] = False


