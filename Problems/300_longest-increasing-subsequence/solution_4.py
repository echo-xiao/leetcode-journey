class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        tail = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            num = nums[i]
            if num > tail[-1]:
                tail.append(num)
            elif num < tail[-1]:
                idx = self.insert(num, tail)
                tail[idx] = num

        return len(tail)

    def insert(self, num: int, tail: List[int]) -> List[int]:
        left, right = 0, len(tail)-1
        while left <= right:
            mid = left + (right - left) // 2
            if tail[mid] >= num:
                right = mid-1
            elif tail[mid] < num:
                left = mid+1
        return left

            