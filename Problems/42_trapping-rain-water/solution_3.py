class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        maxleft = 0
        left = [0] * n
        for i in range(0, n):
            maxleft = max(maxleft, height[i])
            left[i] = maxleft
        
        maxright = 0
        right = [0] * n
        for j in range(n-1, -1, -1):
            maxright = max(maxright, height[j])
            right[j] = maxright
        
        res = 0
        minheight = 0
        for i in range(0, n):
            minheight = min(left[i], right[i])
            res += (minheight - height[i])
        return res