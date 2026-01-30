class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        k, i, j = 0, 0, 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                k += 1
                i += 1
                j += 1
            else:
                j += 1
            print(j, i, k)
        return k
