class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        left, right = 0, len(arr)-1
        while left <= right:
            mid = left + (right - left) // 2
            cnt = arr[mid] - (mid+1)
            if cnt < k:
                left = mid+1
            elif cnt > k:
                right = mid-1
            elif cnt == k:
                right = mid-1

        return k + left