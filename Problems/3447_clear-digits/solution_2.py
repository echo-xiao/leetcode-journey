class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for ele in s:
            if ele.isalpha():
                stack.append(ele)
            elif ele.isdigit():
                if len(stack) > 0:
                    stack.pop()

        return "".join(stack)