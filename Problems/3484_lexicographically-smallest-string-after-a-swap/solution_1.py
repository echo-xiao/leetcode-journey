class Solution:
    def getSmallestString(self, s: str) -> str:
        nums = list(s)
        for i in range(1, len(nums)):
            if int(nums[i-1]) % 2 == int(nums[i]) % 2:
                if int(nums[i-1]) > int(nums[i]):
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                    break
        return "".join(nums)