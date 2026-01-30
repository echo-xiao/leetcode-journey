class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * (n+1)
        for i in range(1, n):
            left[i] = left[i-1] + nums[i-1]
        left = left[0:n]
        
        right = [0] * (n+1)
        for i in range(n-1, -1, -1):
            right[i] = right[i+1] + nums[i]
        right = right[1:]
        
        res = []
        for i in range(0, n):
            res.append(abs(left[i]-right[i]))
        return res