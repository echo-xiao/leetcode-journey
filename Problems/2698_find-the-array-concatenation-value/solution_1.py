class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        num = 0
        while left <= right:
            if left == right:
                num += nums[left]
            else:
                times = 10 ** len(str(nums[right]))
                num = nums[left] * times + nums[right] + num
            left += 1
            right -= 1

        return num

