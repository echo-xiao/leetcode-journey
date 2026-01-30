class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        if len(nums) < 3:
            return False
        
        n = len(nums)
        minArray = [0] * n
        minArray[0] = nums[0]

        for i in range(1, n):
            minArray[i] = min(minArray[i-1], nums[i])

        sortedK = []

        for j in range(n-1, -1, -1):
            if nums[j] > minArray[j]:
                idx = self.binarySearch(sortedK, minArray[j])
                if idx < len(sortedK) and sortedK[idx] < nums[j]:
                    return True
            
            insertPos = self.binarySearch(sortedK, nums[j])
            sortedK.insert(insertPos, nums[j])

        return False

    def binarySearch(self, arr: List[int], target: int):
        left, right = 0, len(arr)

        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left








