class Solution:
    def numberCount(self, a: int, b: int) -> int:
        cnt = 0
        for i in range(a, b+1):
            num = str(i)
            n = len(num)
            if len(num) == len(set(num)):
                cnt += 1
        return cnt