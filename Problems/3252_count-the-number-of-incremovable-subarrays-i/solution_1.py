class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        first = len(nums)-1
        for i in range(0, len(nums)-1):
            if nums[i] >= nums[i+1]:
                first = i
                break
        
        last = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] >= nums[i]:
                last = i
                break
        

        if first == len(nums)-1:
            return len(nums) * (len(nums) + 1) // 2


        ans = len(nums)-last+1
        for i in range(0, first+1):
            left, right = last, len(nums)-1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > nums[i]:
                    right = mid-1
                else:
                    left = mid+1
            ans += (len(nums)-left)+1
        return ans
                