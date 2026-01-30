class Solution(object):
    def captureForts(self, forts):
        """
        :type forts: List[int]
        :rtype: int
        """
        
        max_cnt = 0
        idx = -1

        for i in range(0, len(forts)):
            if forts[i] == 0:
                continue
            if forts[i] == 1 or forts[i] == -1:
                if idx != -1 and forts[i] == forts[idx]:
                    pass
                if idx != -1 and forts[i] != forts[idx]:
                    cnt = i - idx - 1
                    max_cnt = max(max_cnt, cnt)
            idx = i
        return max_cnt
                
