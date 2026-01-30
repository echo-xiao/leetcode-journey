
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:                 # 关键1：用 <，不等于
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                # mid 比右端大 → 右半部分肯定被“砍”过，最小值一定在 mid+1 到 right 之间
                left = mid + 1
                
            elif nums[mid] < nums[right]:
                # mid 比右端小 → 右半部分是严格递增的，最小值一定在 left 到 mid 之间（包括 mid）
                right = mid
                
            else:  # nums[mid] == nums[right]  ← 154 特有情况，无法判断！
                # 只能“安全地扔掉右端一个重复元素”，因为最小值不可能是 right（如果 right 是最小，mid 不可能等于它，除非全数组一样）
                right -= 1
        
        # 循环结束时 left == right，就是最小值的位置
        return nums[left]