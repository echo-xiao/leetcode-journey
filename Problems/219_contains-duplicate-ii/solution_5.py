class Solution(object):
    def containsNearbyDuplicate(self, nums, k):


        seen = set()
        for i in range(0, min(k, len(nums))):
            if nums[i] in seen:
                return True
            else:
                seen.add(nums[i])



        for r in range(k, len(nums)):
            if nums[r] in seen:
                return True
            else:
                seen.add(nums[r])
                seen.remove(nums[r-k])

        return False



                