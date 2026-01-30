class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        curr = [0] * (n+1)

        for i in range(1, n+1):
            curr[i] = curr[i-1] + nums[i-1]

        print(curr)

        cnt = 0
        for i in range(1, n):
            left = curr[i]
            right = curr[-1] - curr[i]
            if (left - right) % 2 == 0:
                cnt += 1
        return cnt
        