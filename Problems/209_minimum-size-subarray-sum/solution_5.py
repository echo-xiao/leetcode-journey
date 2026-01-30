class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        dic = {}
        size = len(nums)
        left, right = 0, 0
        res = 0
        minLen = float('inf')
                

        while right < size:
            res += nums[right]
            right += 1

            while res >= target:
                minLen = min(minLen, right-left)
                
                res -= nums[left]
                left += 1
                
        if minLen == float('inf'):
            return 0
        else:
            return minLen