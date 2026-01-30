class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for char in logs:
            if char == "../":
                if len(stack) > 0:
                    stack.pop()
                else:
                    pass
            elif char == "./":
                pass
            else:
                stack.append(char)
        return len(stack)