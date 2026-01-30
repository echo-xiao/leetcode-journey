# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        return self.helper(n, 1, n)
    
    def helper(self, n: int, left: int, right: int):
        mid = left + (right - left) // 2

        if left > right:
            return left
        
        if isBadVersion(mid) == False:
            return self.helper(n, mid+1, right)
        elif isBadVersion(mid) == True:
            return self.helper(n, left, mid-1)


        return left
        