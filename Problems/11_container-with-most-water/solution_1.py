class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        maxvol = 0
        while left < right:
            vol = min(height[left], height[right]) * (right - left)
            if vol > maxvol:
                maxvol = vol
            if height[left] > height[right]:
                right -= 1
            elif height[left] <= height[right]:
                left += 1
        return maxvol