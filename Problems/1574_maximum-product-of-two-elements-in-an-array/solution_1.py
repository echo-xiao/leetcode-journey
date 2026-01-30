import heapq

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxHeap = []
        for num in nums:
            if len(maxHeap) < 2:
                heapq.heappush(maxHeap, num)
            elif len(maxHeap) == 2:
                heapq.heappushpop(maxHeap, num)

        num1 = heapq.heappop(maxHeap) - 1
        num2 = heapq.heappop(maxHeap) - 1
        return num1 * num2
