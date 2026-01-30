class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_res = -1

        for i in range(0, len(nums)-1):
            left = i + 1
            right = len(nums) - 1
            res = self.helper(nums, k, i, left, right)

            if res != -1:
                curr = nums[i] + nums[res]
                max_res = max(curr, max_res)
        return max_res
    
    def helper(self, nums: List[int], k: int, i: int, left: int, right: int) -> int:
        
        if left > right:
            return -1
            
        mid = left + (right - left) // 2
        curr = nums[i] + nums[mid]

        if curr < k:
            idx = self.helper(nums, k, i, mid+1, right)
            if idx != -1:
                return idx
            else:
                return mid
        else:
            return self.helper(nums, k, i, left, mid-1)
