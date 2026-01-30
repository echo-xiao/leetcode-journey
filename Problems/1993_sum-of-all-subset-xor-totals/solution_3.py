class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        self.res = 0
        self.nums = nums

        self.backtrack(0, 0)

        return self.res

    def backtrack(self, idx, curr):
        if idx == len(self.nums):
            self.res += curr
            return

        self.backtrack(idx+1, curr)
        self.backtrack(idx+1, curr ^ self.nums[idx])

        
