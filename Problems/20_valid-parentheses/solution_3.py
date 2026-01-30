class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for i in s:
            if i in ("(", "[", "{"):
                stack.append(i)
            elif i in (")", "]", "}"):
                if len(stack) == 0:
                    return False
                
                top = stack[-1]
                if (i == ")" and top == "(") or \
                     (i == "]" and top == "[") or \
                     (i == "}" and top == "{"):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
                