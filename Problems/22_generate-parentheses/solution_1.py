class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        path = []

        self.backtrack(0, 0, n, path, res)
        return res

    def backtrack(self, left, right, n, path, res):
        
        if len(path) == 2 * n:
            res.append("".join(path))
            return
        
        if left < n:
            path.append("(")
            self.backtrack(left+1, right, n, path, res)
            path.pop()

        if right < left:
            path.append(")")
            self.backtrack(left, right+1, n, path, res)
            path.pop()

        
        
