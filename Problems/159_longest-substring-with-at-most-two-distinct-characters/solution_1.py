class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        string = "".join(s)
        left, right, maxLen = 0, 0, 0
        res = []

        while right < len(string):
            res.append(string[right])
            right += 1

            while len(set(res)) > 2:
                del res[0]
                left += 1

            maxLen = max(maxLen, right-left)
        return maxLen