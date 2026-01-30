class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False

        charToStr = {}
        strToChar = {}

        for c, w in zip(pattern, words):
            if c in charToStr and charToStr[c] != w:
                return False
            if w in strToChar and strToChar[w] != c:
                return False

            charToStr[c] = w
            strToChar[w] = c
        
        return True