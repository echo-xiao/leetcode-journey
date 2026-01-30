class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        
        i = 0
        j = len(s)
        arr = []

        for k in range(0, len(s)):
            if s[k] == 'I':
                arr.append(i)
                i += 1
            elif s[k] == 'D':
                arr.append(j)
                j -= 1
        arr.append(i)
        return arr