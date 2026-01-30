class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        self.nums = nums
        self.res = 0
        self.backtrack(0, 0)
        return self.res

    
    def backtrack(self, idx: int, curr: int) -> None:
    
        self.res += curr 
        
        for i in range(idx, len(self.nums)):
            self.backtrack(i+1, curr ^ self.nums[i])

