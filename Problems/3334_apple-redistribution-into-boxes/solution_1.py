class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        ttl =sum(apple)
        capacity.sort(reverse=True)
        cnt = 0
        curr = 0

        for i in capacity:
            curr += i
            cnt += 1
            if curr >= ttl:
                break
        return cnt
