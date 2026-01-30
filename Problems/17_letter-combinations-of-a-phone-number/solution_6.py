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

        self.backtrack(0, "", digits, mapping, res)
        return res

    def backtrack(self, index, path, digits, mapping, res):
        if index == len(digits):
            res.append(path)
            return 
        
        letters = mapping[digits[index]]
        for c in letters:
            self.backtrack(index+1, path+c, digits, mapping, res)