class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        res = [0] * len(s)

        tmp = float('-inf') 
        dis = 0
        for i in range(0, len(s)):
            if s[i] == c:
                tmp = i
            dis = i - tmp
            res[i] = dis
        
        tmp = float('inf') 
        for i in range(len(s)-1, -1, -1):
            if s[i] == c:
                tmp = i
            dis = tmp - i
            res[i] = min(dis, res[i])
        
        return res