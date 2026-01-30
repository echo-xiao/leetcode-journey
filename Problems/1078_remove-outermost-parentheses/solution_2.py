class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        cnt = 0

        for char in s:
            if char == "(":
                cnt += 1
                if cnt > 1:
                    res.append(char)
            elif char == ")":
                if cnt > 1:
                    res.append(char)
                cnt -= 1


        return "".join(res)
            
            