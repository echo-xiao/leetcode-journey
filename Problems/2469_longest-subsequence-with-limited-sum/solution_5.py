class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        res = []
        length = -1
        for i in range(0, len(queries)):
            target = queries[i]
            left, right = 0, len(nums)
            while left <= right:
                mid = left + (right - left) // 2
                accu = sum(nums[0:mid])
                if accu <= target:
                    length = mid
                    left = mid +1
                elif accu > target:
                    right = mid - 1
            res.append(length)
        return res