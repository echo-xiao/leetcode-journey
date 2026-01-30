class Solution:
    def queryString(self, s: str, n: int) -> bool:

        if n > 2000:
            return False 
            
        res = []
        for i in range(1, n+1):
            res.append(bin(i)[2:])

        for ele in res:
            if ele not in s:
                return False
        return True
                