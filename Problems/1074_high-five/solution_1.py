import heapq

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        

        students = {}
        
        for idx, score in items:
            if idx not in students:
                students[idx] = []

            heap = students[idx]
            
            if len(heap) < 5:
                heapq.heappush(heap, score)
            elif score > heap[0]:
                heapq.heappushpop(heap, score)

        res = []
        for idx, heap in students.items():
            avg = sum(heap) // 5
            res.append([idx, avg])

        res.sort()
        return res

        

        