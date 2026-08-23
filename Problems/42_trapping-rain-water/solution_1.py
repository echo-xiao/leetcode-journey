class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        res = 0
        maxleft, maxright = 0, 0
        while left < right:
            maxleft = max(maxleft, height[left])
            maxright = max(maxright, height[right])
            if maxleft <= maxright:
                res += (maxleft - height[left])
                left += 1
            else:
                res += (maxright - height[right])
                right -= 1
        return res