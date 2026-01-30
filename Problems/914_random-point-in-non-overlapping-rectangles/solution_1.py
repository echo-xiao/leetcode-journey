class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.prefixSum = []
        ttl = 0

        for a, b, x, y in rects:
            cnt = (x - a + 1) * (y - b + 1)
            ttl += cnt
            self.prefixSum.append(ttl)

        self.ttl = ttl

    def pick(self) -> List[int]:
        target = random.randint(1, self.ttl)

        idx = bisect.bisect_left(self.prefixSum, target)
        a, b, x, y = self.rects[idx]
        pickX = random.randint(a, x)
        pickY = random.randint(b, y)

        return [pickX, pickY]
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()