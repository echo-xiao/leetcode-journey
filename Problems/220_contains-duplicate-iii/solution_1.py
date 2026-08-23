class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:


        if indexDiff <= 0 or valueDiff < 0:
            return False

        w = valueDiff + 1
        buckets = {}                                   # 桶号 -> 桶里那个值

        for i, x in enumerate(nums):
            b = x // w

            # 查：只看三个桶
            if b in buckets:                           # 同桶，必然合格
                return True
            if b - 1 in buckets and abs(x - buckets[b-1]) <= valueDiff:
                return True
            if b + 1 in buckets and abs(x - buckets[b+1]) <= valueDiff:
                return True

            buckets[b] = x                             # 加

            if i >= indexDiff:                         # 修
                del buckets[nums[i - indexDiff] // w]

        return False