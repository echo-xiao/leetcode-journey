class Solution:
    def mySqrt(self, x: int) -> int:
        
        left, right = 1, x
        res = 0


        while left <= right:
            mid = left + (right - left) // 2

            if mid * mid == x:            
                return mid
            elif mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                res = mid
                left = mid + 1


        return res
        