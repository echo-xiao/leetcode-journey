class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        stack = []
        res = 0
        for i in range(0, n):
            while len(stack) > 0 and height[i] > height[stack[-1]]:
                bottom = stack.pop()

                if len(stack) == 0:
                    break

                left = height[stack[-1]]
                right = height[i]
                wall = min(left, right) - height[bottom]
                length = i - stack[-1] - 1
                res += wall * length
            stack.append(i)
        return res