class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        ttl = sum(cardPoints)
        minnum = 0
        num = 0
        length = n-k

        if n <= length:
            return ttl
        
        for i in range(0, length):
            num += cardPoints[i]
        minnum = num
        
        for i in range(length, n):
            num += cardPoints[i]
            num -= cardPoints[i-length]

            minnum = min(minnum, num)
        return ttl - minnum

