class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        res = self.helper(nums, 0, len(nums))
        if res is None:
            return -1
        else:
            return res

    def helper(self, nums: List[int], left: int, right: int) -> int:

        if left > right:
            return 

        guess = left + (right - left) // 2
        cnt = 0
        for num in nums:
            if num >= guess:
                cnt += 1
        if cnt == guess:
            return guess
        elif cnt > guess:
            return self.helper(nums, guess+1, right)
        else:
            return self.helper(nums, left, guess-1)