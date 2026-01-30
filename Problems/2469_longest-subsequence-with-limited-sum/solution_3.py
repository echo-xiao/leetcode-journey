class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]: 
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        res = []
        for i in range(0, len(queries)):
            target = queries[i]
            curr = self.helper(nums, target, 0, len(nums)-1)
            res.append(curr)
        return res
        


    def helper(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left > right:
            return left

        mid = left + (right - left) // 2
        if nums[mid] > target:
            return self.helper(nums, target, left, mid-1)
        else:
            return self.helper(nums, target, mid+1, right)