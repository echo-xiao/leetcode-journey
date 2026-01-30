class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        minHeap = []
        arr = []
        for num in nums:
            heapq.heappush(minHeap, num)

        while minHeap:
            num1 = heapq.heappop(minHeap)
            num2 = heapq.heappop(minHeap)
            arr.append(num2)
            arr.append(num1)
        return arr