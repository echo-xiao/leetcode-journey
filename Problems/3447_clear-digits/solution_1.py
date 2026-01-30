class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for element in s:
            if element.isalpha():
                stack.append(element)
            elif element.isdigit():
                if len(stack) > 0:
                    stack.pop()
        return "".join(stack)