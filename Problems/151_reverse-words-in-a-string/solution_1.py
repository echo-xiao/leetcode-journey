class Solution:
    def reverseWords(self, s: str) -> str:
        s += " "

        tmp = ""        
        lst = []
        for c in s:
            if c != " ":
                tmp += c
            elif tmp:
                lst.append(tmp)
                tmp = ""
        return " ".join(reversed(lst))
