class Solution:
    def isValid(self, s: str) -> bool:

        mapp = {
            ')': '(', 
            ']': '[', 
            '}': '{'
            }
        stack = []

        for char in s:
            if char in mapp:
                if len(stack) == 0:
                    return False
                    
                top = stack.pop()

                if mapp[char] != top:
                    return False
            
            else:
                stack.append(char)
        
        if len(stack) == 0:
            return True
        else:
            return False