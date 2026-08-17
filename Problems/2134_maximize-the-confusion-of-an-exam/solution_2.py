class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        maxlen = 0
        n = len(answerKey)
        for c in ('T', 'F'):
            left, right = 0, 0
            cnt = 0
            for right in range(0, n):
                if answerKey[right] == c:
                    cnt += 1
                while cnt > k:
                    if answerKey[left] == c:
                        cnt -= 1
                    left += 1
                maxlen = max(maxlen, right-left+1)
        return maxlen
            
