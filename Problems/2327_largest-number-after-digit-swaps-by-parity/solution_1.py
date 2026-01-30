class Solution:
    def largestInteger(self, num: int) -> int:
        oddHeap = []
        evenHeap = []

        for i in str(num):
            if int(i) % 2 == 0:
                heappush(evenHeap, -int(i))
            else:
                heappush(oddHeap, -int(i))

        res = []
        for j in str(num):
            if int(j) % 2 == 0:
                res.append(str(-heappop(evenHeap)))
            else:
                res.append(str(-heappop(oddHeap)))

        return int("".join(res))