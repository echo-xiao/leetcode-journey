class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        res = 0
        hasOdd = False
        for val, cnt in dic.items():
            if cnt % 2 == 0:
                res += cnt
            else:
                res += (cnt - 1)
                hasOdd = True
        
        if hasOdd == True:
            return res+1
        else:
            return res
                