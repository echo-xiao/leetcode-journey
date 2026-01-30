class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        
        first = -1
        for i in range(0, len(nums)):
            if nums[i] == target:
                first = i
                break

        if first == -1: 
            return False

    
        left = first
        right = len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                last = mid
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
        
        res = last - first + 1
        if res > len(nums) // 2:
            return True
        else:
            return False

                    
