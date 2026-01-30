class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = collections.Counter(s)
        oddCnt = 0
        for value, cnt in counter.items():
            if cnt % 2 == 1:
                oddCnt += 1
                if oddCnt > 1:
                    return False
        return True