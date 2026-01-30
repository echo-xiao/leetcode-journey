import heapq

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        arr = []
        ttl = 0

        for row in range(len(grid)):
            maxHeap = []
            for val in grid[row]:
                heapq.heappush(maxHeap, -val)
            arr.append(maxHeap)

        for idx in range(0, len(arr[0])):
            deleted = []
            for h in range(len(arr)):
                heap = arr[h]
                maxVal = -heapq.heappop(heap)
                deleted.append(maxVal)
            res = max(deleted)
            ttl += res

        return ttl
        