class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        

        maxHeap = []
        for idx in range(0, len(mat)):
            cnt = sum(mat[idx])
            item = [-cnt, -idx]

            if len(maxHeap) < k:
                heappush(maxHeap, item)    
            else:
                heappushpop(maxHeap, item)
        
        res = []
        while maxHeap:
            cnt, idx = heapq.heappop(maxHeap)
            res.append(-idx)
        return res[::-1]

