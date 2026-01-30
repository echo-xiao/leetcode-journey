class Solution(object):
    def sortedSquares(self, A):

    
        result = []
        for i in range(len(A)):
            print(A[0], A[-1])
            if A[0]**2 < A[-1]**2:
                result.insert(0, A[-1]**2)
                A.pop(-1)
            else:
                result.insert(0, A[0]**2)
                A.pop(0)
        return result