class Solution(object):
    def containsNearbyDuplicate(self, nums, k):


        seen = set()
        for j in range(0, len(nums)):
            if nums[j] in seen:
                return True
            else:
                seen.add(nums[j])
            
            if len(seen) > k:
                seen.remove(nums[j-k])
        return False


        # 两种解法，一种哈希表法，一种是滑动窗口



                