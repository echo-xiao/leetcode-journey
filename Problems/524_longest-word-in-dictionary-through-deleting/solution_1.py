class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        

        res = ""
        for key in dictionary:
            n = len(key)
            left = 0
            right = 0
            while left < len(s) and right < len(key):
                if key[right] == s[left]:
                    right += 1
                left += 1
            if right == len(key):
                if len(key) > len(res) or (len(key) == len(res) and key < res):
                    res = key
        return res
            