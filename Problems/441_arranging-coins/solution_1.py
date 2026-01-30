class Solution:
    def arrangeCoins(self, n: int) -> int:
        return self.helper(n, 1, n)
        

    def helper(self, n: int, left: int, right: int) -> int:
        while left > right:
            return right 

        mid = left + (right - left) // 2
        cnt = (1 + mid) * mid / 2
        if cnt == n:
            return mid
        elif cnt > n:
            return self.helper(n, left, mid-1)
        elif cnt < n:
            return self.helper(n, mid+1, right)
    
