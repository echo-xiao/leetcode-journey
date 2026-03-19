class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        string = "".join(s)
        size = len(string)
        left, right = 0, 0
        maxLen = 0
        res = []


        while right < size:
            res.append(string[right])
            right += 1

            while len(set(res)) > k:
                del res[0]
                left += 1

            maxLen = max(maxLen, right-left)

        return maxLen