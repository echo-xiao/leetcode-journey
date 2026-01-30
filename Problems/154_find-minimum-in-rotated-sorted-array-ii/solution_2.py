
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:                
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
                
            elif nums[mid] < nums[right]:
                right = mid
                
            else:  
                
                right -= 1
        
        # 循环结束时 left == right，就是最小值的位置
        return nums[left]