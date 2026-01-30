class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        res = self.helper(arr, k, 0, len(arr)-1)
        return k + res

    def helper(self, arr: List[int], k: int, left: int, right: int) -> int:
        if left > right:
            return left

        mid = left + (right - left) // 2
        cnt = arr[mid] - (mid+1)
        if cnt >= k:
            return self.helper(arr, k, left, mid-1)
        else:
            return self.helper(arr, k, mid+1, right)
        