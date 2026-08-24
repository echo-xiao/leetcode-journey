class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        
        seen = set()
        for i in range(0, len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
            if len(seen) > k:
                seen.remove(nums[i-k])
        return False