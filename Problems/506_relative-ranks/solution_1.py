

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        maxHeap = []

        for idx, val in enumerate(score):
            item = (-val, idx)
            heapq.heappush(maxHeap, item)
        
        res = [0] * len(score)
        place = 1
        while maxHeap:
            pos = heapq.heappop(maxHeap)[1]
            if place == 1:
                rk = 'Gold Medal'
            elif place == 2:
                rk = 'Silver Medal'
            elif place == 3:
                rk = 'Bronze Medal'
            elif place > 3:
                rk = str(place)
            
            res[pos] = rk
            place += 1
        return res