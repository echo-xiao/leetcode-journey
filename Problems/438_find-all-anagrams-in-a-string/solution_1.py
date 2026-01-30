class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        pCount = {}
        sCount = {}

        for char in p:
            pCount[char] = 1 + pCount.get(char, 0)

        left, right = 0, 0
        res = []

        while right < len(s):
            c = s[right]
            sCount[c] = 1 + sCount.get(c, 0)
            right += 1

            while right - left >= len(p):
                if pCount == sCount:
                    res.append(left)
                l = s[left]
                sCount[l] -= 1
                if sCount[l] == 0:
                    del sCount[l]
                left += 1
        return res
