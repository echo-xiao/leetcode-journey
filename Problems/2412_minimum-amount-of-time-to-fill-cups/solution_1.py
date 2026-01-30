class Solution:
    def fillCups(self, amount: List[int]) -> int:
        
        maxHeap = []
        for i in amount:
            if i > 0:
                heappush(maxHeap, -i)
        
        cnt = 0
        while maxHeap:
            if len(maxHeap) >= 2:
                num1 = heappop(maxHeap) + 1
                num2 = heappop(maxHeap) + 1
                if num1 < 0: 
                    heappush(maxHeap, num1)
                if num2 < 0:
                    heappush(maxHeap, num2)
                cnt += 1
            else:
                num = heappop(maxHeap) + 1
                if num < 0:
                    heappush(maxHeap, num)
                cnt += 1
                
        return cnt 

