class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        min_idx = 0
        max_idx = 0
        n = len(nums)

        for j in range(indexDifference, n):
            i = j - indexDifference

            if nums[i] < nums[min_idx]:
                min_idx = i
            if nums[i] > nums[max_idx]:
                max_idx = i

            if abs(nums[j] - nums[min_idx]) >= valueDifference:
                return [min_idx, j]
            
            if abs(nums[j] - nums[max_idx]) >= valueDifference:
                return [max_idx, j]

        return [-1, -1]