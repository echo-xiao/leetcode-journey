class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        curr =[0] * (n+1)
        for i in range(0, n):
            curr[i+1] = curr[i] + gain[i]
        return max(curr)