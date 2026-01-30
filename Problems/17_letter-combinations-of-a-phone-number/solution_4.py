class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        self.backtrack(0, [], digits, mapping, res)
        return res

    def backtrack(self, depth, path, digits, mapping, res):
        if depth == len(digits):
            res.append("".join(path))
            return 
        
        letters = mapping[digits[depth]]
        for c in letters:
            path.append(c)
            self.backtrack(depth+1, path, digits, mapping, res)
            path.pop()