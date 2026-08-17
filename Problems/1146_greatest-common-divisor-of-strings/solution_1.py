class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        g = self.gcd(l1, l2)
        cand = str1[:g]
        if cand * (l1 // g) == str1 and cand * (l2 // g) == str2:
            return cand
        else:
            return ""
        
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a