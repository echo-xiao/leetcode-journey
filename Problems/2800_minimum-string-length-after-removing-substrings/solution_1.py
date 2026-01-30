class Solution:
    def minLength(self, s: str) -> int:
        
        stack = []

        for char in s:
            if len(stack) > 0:
                top = stack[-1]
                if top == 'A' and char == 'B':
                    stack.pop()
                elif top == 'C' and char == 'D':
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        return len(stack)
