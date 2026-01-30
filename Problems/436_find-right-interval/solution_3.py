class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        

        arr = []

        for i in range(0, len(intervals)):
            arr.append((intervals[i][0], i))

        arr.sort(key=lambda x: x[0])
        res = []

        for i in range(0, len(intervals)):
            target = intervals[i][1]
            idx = self.binarySearch(arr, target)
            res.append(idx)
        return res

    def binarySearch(self, arr: List[int], target: int) -> List[list[int]]:
        left, right = 0, len(arr)-1
        tag = -1
        while left <= right:
            mid = left + (right - left) // 2
            start = arr[mid][0]
            idx = arr[mid][1]
            if start >= target:
                tag = idx
                right = mid - 1
            else:
                left = mid + 1
        return tag