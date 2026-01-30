class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        minHeap = []

        for num in nums:
            if num > 0:
                heappush(minHeap, num)

        last, cnt = 0, 0
        while minHeap:
            curr = heappop(minHeap)
            if curr > last:
                cnt += 1
                last = curr
        return cnt