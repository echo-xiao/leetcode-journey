class Solution:
    def mySqrt(self, x: int) -> int:
        return self.helper(x, 0, x)
        

    def helper(self, x: int, left: int, right: int) -> int:
        if left > right:
            return right

        mid = left + (right - left) // 2

        if mid * mid == x:
            return mid
        elif mid * mid > x:
            return self.helper(x, left, mid-1)
        elif mid * mid < x:
            return self.helper(x, mid+1, right)


