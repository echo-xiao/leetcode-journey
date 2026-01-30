class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        self.res = -1

        for i in range(0, len(nums)-1):
            left = i + 1
            right = len(nums) - 1
            self.helper(nums, k, i, left, right)
        return self.res
    
    def helper(self, nums: List[int], k: int, i: int, left: int, right: int) -> int:
        
        if left > right:
            return 
            
        mid = left + (right - left) // 2
        curr = nums[i] + nums[mid]

        if curr < k:
            self.res = max(curr, self.res)
            self.helper(nums, k, i, mid+1, right)
        else:
            self.helper(nums, k, i, left, mid-1)
