class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        cnt = 0
        arr = set(nums)
        if 0 in arr:
            return len(arr)-1
        else:
            return len(arr)