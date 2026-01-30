class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        n = len(nums)
        cnt = 0

        prefix = [0] * n
        suffix = [0] * n
        
        # Build prefix sums
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i - 1]

        # Build suffix sums
        for i in reversed(range(n - 1)):
            suffix[i] = suffix[i + 1] + nums[i + 1]

        for i, num in enumerate(nums):
            if num != 0:
                continue

            # Both sides will be zero at the same time
            if prefix[i] == suffix[i]:
                cnt += 2

            # Only one side will be zero at the end
            if abs(prefix[i] - suffix[i]) == 1:
                cnt += 1

        return cnt