class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        arr = [0] * (len(nums)+1)

        for i in range(0, len(nums)):
            arr[i+1] = arr[i] + nums[i]

        res = float('inf')
        for i in range(0, len(nums)):
            val = arr[i] + target
            left, right = i+1, len(nums)
            bound=-1

            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] >= val:
                    bound = mid
                    right = mid - 1
                elif arr[mid] < val:
                    left = mid + 1

            if bound != -1:
                res = min(res, bound-i)

        if res == float('inf'):
            return 0
        else:
            return res
