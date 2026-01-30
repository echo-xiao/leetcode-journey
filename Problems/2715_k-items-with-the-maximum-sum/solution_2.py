class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes:
            return k

        else:
            if k - numOnes <= numZeros:
                return numOnes
            else:
                forced_neg_ones_count = k - numOnes - numZeros
                
                # 最终总和 = (拿 1 的总和) - (被迫拿 -1 的数量)
                return numOnes - forced_neg_ones_count