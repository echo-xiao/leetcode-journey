class Solution:
    def reverseVowels(self, s: str) -> str:
        idx = []
        res = []
        s = list(s)

        for i in range(0, len(s)):
            if s[i].lower() in ('a', 'e', 'i', 'o', 'u'):
                idx.append(i)
                res.append(s[i])
        
        for j in idx:
            val = res.pop()
            s[j] = val
        
        return "".join(s)