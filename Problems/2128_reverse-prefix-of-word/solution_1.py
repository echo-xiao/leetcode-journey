class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        stack = []
        try:
            idx = word.index(ch)
        except ValueError:
            return word


        for i in range(0, idx+1):
            stack.append(word[i])

        res = []
        while len(stack) > 0:
            res.append(stack.pop())
        
        return "".join(res) + word[idx+1:]
            