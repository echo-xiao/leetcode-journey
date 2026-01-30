class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        cnt = list(dic.values())
        cnt.sort()
        
        n = len(cnt)
        l = n - k

        if l <= 0:
            return 0

        return sum(cnt[:l])
