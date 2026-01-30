class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes:
            return k

        else:
            if k - numOnes <= numZeros:
                return numOnes
            else:
                if k - numOnes - numZeros <= numNegOnes:
                    return numOnes - (k - numOnes - numZeros)
                else:
                    return numOnes - numNegOnes