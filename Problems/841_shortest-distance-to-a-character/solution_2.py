class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        arr = []
        for i in range(0, len(s)):
            if s[i] == c:
                arr.append(i)
        
        res = [0] * len(s)
        for i in range(0, len(s)):
            min_dis = 10000000000
            for c in range(0, len(arr)):
                dis = abs(i - arr[c])
                min_dis = min(min_dis, dis)
            res[i] = min_dis
        return res