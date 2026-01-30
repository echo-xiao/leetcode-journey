class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        curr = [0] * (len(nums)+1)
        for i in range(0, len(nums)):
            curr[i+1] = curr[i] + nums[i]

        for j in range(0, len(nums)):
            left = curr[j]
            right = curr[-1] - curr[j+1]
            if left == right:
                return j
        return -1