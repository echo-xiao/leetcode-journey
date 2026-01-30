class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        arr = [0] * (n + 1)
        for i in range(0, n):
            arr[i+1] = arr[i] + nums[i]

        minLen = float('inf')

        for i in range(0, n):
            val = target + arr[i]

            left, right = i+1, n
            bound = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] >= val:
                    bound = mid
                    right = mid - 1
                else:
                    left = mid + 1
            if bound != -1:
                minLen = min(minLen, bound-i)

        return 0 if minLen == float('inf') else minLen