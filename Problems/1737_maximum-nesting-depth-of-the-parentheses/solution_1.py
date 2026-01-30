class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxRes = 0
        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")":
                stack.pop()
            else:
                pass
            res = len(stack)
            maxRes = max(res, maxRes)
        return maxRes
            