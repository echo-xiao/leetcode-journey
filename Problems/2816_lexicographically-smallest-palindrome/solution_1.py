class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        
        string = list(s)
        i = 0
        j = len(s) - 1

        while i < j:
            if ord(string[i]) < ord(string[j]):
                string[j] = string[i]
            elif ord(string[i]) > ord(string[j]):
                string[i] = string[j]
            i += 1
            j -= 1
        return "".join(string)
                