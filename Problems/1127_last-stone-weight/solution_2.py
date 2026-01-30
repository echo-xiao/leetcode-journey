class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for s in stones:
            heapq.heappush(maxHeap, -s)

        while len(maxHeap)>1:
            y = heapq.heappop(maxHeap)
            x = heapq.heappop(maxHeap)

            if x != y:
                heapq.heappush(maxHeap, y-x)

        if not maxHeap:
            return 0
        else:
            return -maxHeap[0]
