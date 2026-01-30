class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """

        n = len(blocks)
        i = 0
        cnt = 0
        min_cnt  = 1000000
        win = blocks[0: k]
        for e in win:
            if e == 'W':
                cnt += 1
        min_cnt = min(cnt, min_cnt)

        for j in range(k, n):
            win = blocks[i+1: i+k+1]
            if blocks[j] == 'W':
                cnt += 1
            if blocks[i] == 'W':
                cnt -= 1
            min_cnt = min(cnt, min_cnt)
            i += 1
        return min_cnt

        