class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        minHeap = []
        for idx, val in enumerate(nums):
            item = (val, idx)
            heapq.heappush(minHeap, item)

        for i in range(k):
            minVal, currIdx = heapq.heappop(minHeap)
            newItem = minVal * multiplier, currIdx
            heapq.heappush(minHeap, newItem)
        
        arr = [0] * len(nums)
        for val, idx in minHeap:
            arr[idx] = val

        return arr