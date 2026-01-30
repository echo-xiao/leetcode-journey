class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) < 3:
            return 0 


            
        seen = set()
        left = 0
        win = s[0: 3]
        if len(set(win)) == len(win):
            cnt = 1
        else:
            cnt = 0
        
        

        for right in range(3, len(s)):
            win = s[left+1: right+1]

            if len(set(win)) == len(win):
                cnt += 1
            
            left += 1
        return cnt
            
