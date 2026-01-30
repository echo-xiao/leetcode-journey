class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        sett = list(set(nums))
        sett.sort(reverse=True)
        res = []
        for i in range(0, len(sett)):
            if i < k:
                res.append(sett[i])
            else:
                break
        return res