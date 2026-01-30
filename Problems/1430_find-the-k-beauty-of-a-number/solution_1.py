class Solution(object):
    def divisorSubstrings(self, num, k):

        org = num
        num = str(num)
        n = len(num)
        cnt = 0

        for i in range(0, n-k+1):
            sub = num[i: i+k]
            if int(sub) != 0 and org % int(sub) == 0:
                cnt += 1
        return cnt