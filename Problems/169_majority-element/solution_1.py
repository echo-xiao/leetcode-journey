class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
                    
        mid = len(nums) // 2
        left = self.majorityElement(nums[0: mid])
        right = self.majorityElement(nums[mid: ])

        if nums.count(left) >= nums.count(right):
            return left
        else:
            return right
