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
    
        self.dfs(digits, 0, [], mapping, res)
        return res



    def dfs(self, digits, idx, path, mapping, res):
        if idx == len(digits):
            res.append("".join(path))
            return 

        num = digits[idx]
        letters = mapping[num]

        for c in letters:
            path.append(c)
            self.dfs(digits, idx+1, path, mapping, res)
            path.pop()

            