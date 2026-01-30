class Solution:
    def makeGood(self, s: str) -> str:
        
        stack = []
        for char in s:
            if len(stack) > 0:
                peek = stack[-1]
                if peek.lower() == char.lower() and peek != char:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        return "".join(stack)