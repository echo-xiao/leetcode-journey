class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        vol, maxvol = 0, 0 
        while left < right:
            vol = (right-left) * min(height[right], height[left])
            maxvol = max(maxvol, vol)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

            
        return maxvol
