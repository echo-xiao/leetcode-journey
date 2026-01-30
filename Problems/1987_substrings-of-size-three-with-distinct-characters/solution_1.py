class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) < 3:
            return 0 


            
        seen = set()
        win = s[0: 3]
        if len(set(win)) == len(win):
            cnt = 1
        else:
            cnt = 0
        
        for right in range(3, len(s)):
            win = s[right-2: right+1]

            if len(set(win)) == len(win):
                cnt += 1
            
        return cnt
            
