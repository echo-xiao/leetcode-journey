class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        return self.helper(arr, 0, len(arr)-1)
        
    def helper(self, arr: List[int], left: int, right: int) -> int:
        res = -1
        if left > right:
            return res

        mid = left + (right - left) // 2
        if arr[mid] == mid:
            idx = self.helper(arr, left, mid-1)
            if idx != res:
                return idx
            else:
                return mid
        elif arr[mid] > mid:
            return self.helper(arr, left, mid-1)
        elif arr[mid] < mid:
            return self.helper(arr, mid+1, right)