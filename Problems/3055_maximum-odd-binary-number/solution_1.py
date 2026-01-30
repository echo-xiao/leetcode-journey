class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        nums = list(s)
        n = len(nums)
        cnt = 0
        for i in nums:
            if i == '1':
                cnt += 1

        nums[-1] = '1'
        rem = cnt - 1
        nums[0:rem] = ['1'] * rem
        left = n - 1 - rem
        nums[rem: -1] = ['0'] * left

        return "".join(nums)