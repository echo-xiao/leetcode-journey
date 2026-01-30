class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        return self.helper(num, 1, num)

    def helper(self, num: int, left: int, right: int) -> bool:
        
        if left > right:
            return False

        mid = left + (right - left) // 2

        if mid * mid == num:
            return True
        elif mid * mid > num:
            return self.helper(num, left, mid - 1)
        elif mid * mid < num:
            return self.helper(num, mid + 1, right)

