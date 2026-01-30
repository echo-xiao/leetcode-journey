class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = []
        for i in range(0, n+1):
            num = bin(i)
            cnt = num.count('1')
            res.append(cnt)
        return res