class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        mapp = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for char in s:
            if char in mapp:
                stack.append(mapp[char])
            else:
                if len(stack) > 0:
                    top = stack[-1]
                    if top == char:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False

                
