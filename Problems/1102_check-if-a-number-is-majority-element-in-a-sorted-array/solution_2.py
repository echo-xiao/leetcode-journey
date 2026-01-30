class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        self.last = -1
        first = -1
        for i in range(0, len(nums)):
            if nums[i] == target:
                first = i
                break

        if first == -1:
            return False
        
        left = first 
        right = len(nums)-1
        
        last = self.helper(nums, target, left, right)

        dis = self.last - first + 1
        if dis > len(nums) / 2:
            return True
        else:
            return False

    def helper(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left > right:
            return self.last

        mid = left + (right - left) // 2
        if nums[mid] == target:
            self.last = mid
            return self.helper(nums, target, mid+1, right)
        elif nums[mid] > target:
            return self.helper(nums, target, left, mid-1)

        
        