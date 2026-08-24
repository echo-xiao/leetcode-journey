class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = "".join(s)
        size = len(string)
        left, right = 0, 0
        res =[]
        maxLen = 0

        while right < size:
            res.append(string[right])
            right += 1
            
            while len(res) != len(set(res)):
                del res[0]
                left += 1
            
            maxLen = max(maxLen, right-left)

        return maxLen