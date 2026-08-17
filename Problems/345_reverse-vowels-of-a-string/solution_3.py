class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        lst = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i, j = 0, len(s)-1
        while i < j:
            if s[i] in lst and s[j] in lst:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif s[i] in lst:
                j -= 1
            elif s[j] in lst:
                i += 1
            else:
                i += 1
            
        return "".join(s)
        