class Solution(object):
    def removeElement(self, nums, val):
        
        slow = 0
        for fast in range(0, len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return len(nums[0:slow])
        