class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            if len(stack) > 0:
                curr = stack[-1]
                if curr == char:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        return "".join(stack)
