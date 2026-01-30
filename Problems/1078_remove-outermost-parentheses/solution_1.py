class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        res = []

        for char in s:
            if char == "(":
                if len(stack) > 0:
                    res.append(char)
                stack.append(char)

            elif char == ')':
                if len(stack) > 1:
                    res.append(char)
                
                stack.pop()
        
        return "".join(res)