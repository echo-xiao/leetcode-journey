class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        curr = [0] * 101

        for start, end in nums:
            curr[start] += 1
            if end + 1 < len(curr):
                curr[end+1] -= 1


        res = 0
        cnt = 0

        for i in range(0, len(curr)):
            res += curr[i]
            if res > 0:
                cnt += 1
        return cnt
