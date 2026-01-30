class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        ttl = 0
        rows = len(grid)
        cols = len(grid[0])
        
        if rows == 0:
            return 0

        for j in range(cols):
            arr = []
            for i in range(rows):
                arr.append(grid[i][j])
            cal = self.cntOperation(arr)
            ttl += cal
        return ttl
        
        
    def cntOperation(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                target = nums[i-1] + 1
                needed = target - nums[i]
                cnt += needed
                nums[i] = target
        return cnt
                