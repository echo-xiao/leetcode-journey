class Solution(object):
    def removeDuplicates(self, nums):
        slow = 0
        for fast in range(0, len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        return len(nums[0:slow+1])