class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for num in operations:
            
            if num == 'D':
                prev = stack.pop()
                stack.append(prev)
                stack.append(prev * 2)

            elif num == 'C':
                stack.pop()

            elif num == '+':
                prev1 = stack.pop()
                prev2 = stack.pop()
                stack.append(prev2)
                stack.append(prev1)
                stack.append(prev1 + prev2)

            else:
                stack.append(int(num))

        return sum(stack)