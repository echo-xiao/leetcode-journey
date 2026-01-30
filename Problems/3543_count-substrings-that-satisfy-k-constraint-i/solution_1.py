class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        cnt = 0
        seen = {'0': 0, '1': 0}
        l = 0
        

        for r in range(0, len(s)):
            if s[r] not in seen:
                seen[s[r]] = 1
            else:
                seen[s[r]] += 1

            while seen['0'] > k and seen['1'] > k:
                seen[s[l]] -= 1
                l += 1

            cnt += r - l + 1
            
        return cnt
            