class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0
        self.backtrack(0, nums, 0)
        return self.res

    
    def backtrack(self, idx: int, nums: List[int], curr: int) -> None:
    
        self.res += curr 
        
        for i in range(idx, len(nums)):
            
            self.backtrack(i+1, nums, curr ^ nums[i])

