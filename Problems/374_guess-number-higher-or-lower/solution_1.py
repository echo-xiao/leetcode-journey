# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        return self.helper(n, 1, n)

        
    def helper(self, n: int, left: int, right: int) -> int:

        mid = left + (right - left) // 2
        
        if guess(mid) == 0:
            return mid
        elif guess(mid) == -1:
            return self.helper(n, left, mid-1)
        elif guess(mid) == 1:
            return self.helper(n, mid+1, right)


        