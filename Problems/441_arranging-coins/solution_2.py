class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = left + (right - left) // 2
            cnt = (1 + mid) * mid / 2
            if cnt == n:
                return mid
            elif cnt > n:
                right = mid - 1
            elif cnt < n:
                left = mid + 1
        return right