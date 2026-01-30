class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        minHeap = []
        for idx, num in enumerate(nums):
            item = [num, idx]
            if len(minHeap) < k:
                heappush(minHeap, item)
            elif len(minHeap) == k:
                heappushpop(minHeap, item)
        sortedHeap = sorted(minHeap, key = lambda x: x[1])
        return [val for val, idx in sortedHeap]
            
        
