class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        n1 = len(s)
        n2 = len(spaces)
        n = n1 + n2
        i, j, k = n1-1, n2-1, n-1
        res = [""] * n

        
        while i >= 0:
            res[k] = s[i]
            k -= 1

            if j >= 0 and i == spaces[j]:
                res[k] = " "
                j -= 1
                k -= 1
            i -= 1
            
        
        return "".join(res)
