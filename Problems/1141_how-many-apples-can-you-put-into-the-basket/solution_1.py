class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        target = 5000
        accu = 0
        cnt = 0
        for w in weight:
            if accu + w <= target:
                accu += w
                cnt += 1
            else:
                break
        return cnt