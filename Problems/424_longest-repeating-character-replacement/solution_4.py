class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        



        dic = {}
        maxCount = 0

        right, left = 0, 0
        res = []
        maxLen = 0
        while right < len(s):
            char = s[right]
            res.append(s[right])
            
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1

            maxCount = max(dic[char], maxCount)
            right += 1

            while len(res) - maxCount > k:
                dic[res[0]] -= 1
                del res[0]
                left += 1

            maxLen = max(maxLen, right - left)

        return maxLen

