class Solution:
    def reverseBits(self, n: int) -> int:
        

        arr = []
        res = 0
        
        for _ in range(0, 32):
            k = n % 2
            arr.append(k)
            n = n // 2
        
        
        for i in arr:
            res = res * 2 + i

        return res