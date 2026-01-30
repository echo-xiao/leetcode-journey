class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        res = []
        length = -1
        for i in range(0, len(queries)):
            target = queries[i]
            left, right = 0, len(nums)-1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid +1
                elif nums[mid] > target:
                    right = mid - 1
            res.append(left)
        return res