class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        minHeap = []

        for num in nums:
            if num > 0:
                heappush(minHeap, num)

        actual, ttl, cnt = 0, 0, 0
        while minHeap:
            curr = heappop(minHeap)
            actual = curr - ttl
            if actual > 0:
                cnt += 1
                ttl += actual
        return cnt