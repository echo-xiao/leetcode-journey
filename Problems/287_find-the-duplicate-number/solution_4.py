class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        left, right = 1, n

        while left <= right:
            mid = left + (right - left) // 2
            cnt = self.cntLessThanMid(nums, mid)
            if cnt > mid:
                right = mid-1
            else:
                left = mid+1
        return left

    def cntLessThanMid(self, nums: List[int], mid: int) -> int:
        cnt = 0
        for n in nums:
            if n <= mid:
                cnt += 1
        return cnt
            