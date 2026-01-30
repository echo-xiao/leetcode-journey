class Solution(object):
    def sortedSquares(self, A):
        res = []
        for i in range(len(A)):
            if A[0]**2 > A[-1]**2:
                res.insert(0, A[0]**2)
                A.pop(0)
            else:
                res.insert(0, A[-1]**2)
                A.pop(-1)
        return res

    
