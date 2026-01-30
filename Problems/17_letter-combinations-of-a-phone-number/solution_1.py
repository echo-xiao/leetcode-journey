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
        path = []
        self.dfs(digits, 0, path, res, mapping)
        return res


    def dfs(self, digits, i, path, res, mapping):
        if len(path) == len(digits):
            res.append("".join(path))
            return

        num = digits[i]
        for c in mapping[num]:
            path.append(c)
            self.dfs(digits, i+1, path, res, mapping)
            path.pop()

