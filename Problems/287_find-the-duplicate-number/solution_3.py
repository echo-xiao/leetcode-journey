class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        left, right = 1, len(nums)-1
        ans = -1

        while left <= right:
            mid = left + (right - left) // 2
            cnt = self.findCnt(nums, mid)

            if cnt > mid:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def findCnt(self, nums: List[int], mid: int) -> int:
        cnt = 0
        for num in nums:
            if num <= mid:
                cnt += 1
        return cnt