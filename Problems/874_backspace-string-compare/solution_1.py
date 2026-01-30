class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.buildStack(s) == self.buildStack(t)

    def buildStack(self, nums: str) -> str:

        stack = []

        for n in nums:
            if n != '#':
                stack.append(n)
            elif len(stack) > 0:
                stack.pop()
        return stack