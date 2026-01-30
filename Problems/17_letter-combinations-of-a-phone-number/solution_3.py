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

    def backtrack(self, idx, path, digits, mapping, res):
        if idx == len(digits):
            res.append("".join(path))
            return 
        
        letters = mapping[digits[idx]]
        for c in letters:
            path.append(c)
            self.backtrack(idx+1, path, digits, mapping, res)
            path.pop()