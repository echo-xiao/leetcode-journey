class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxHeap = []
        for g in gifts:
            heapq.heappush(maxHeap, -g)
        
        for i in range(0, k):
            maxVal = heapq.heappop(maxHeap)
            leftVal = floor(sqrt(-maxVal))
            heapq.heappush(maxHeap, -leftVal)

        return -sum(maxHeap)