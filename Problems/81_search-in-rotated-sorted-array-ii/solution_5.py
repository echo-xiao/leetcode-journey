class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        pivot = self.findPivotIndex(nums)
        return self.binarySearch(nums, 0, pivot - 1, target) or self.binarySearch(nums, pivot, len(nums) - 1, target)



    def findPivotIndex(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # 兜底逻辑：如果区间缩到一个点，那就是它了
            # 这一行是配合 left <= right 的关键，防止无限循环
            if left == right:
                return left
                
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                # 中间 > 右边：断崖在右侧
                left = mid + 1
            elif nums[mid] < nums[right]:
                # 中间 < 右边：右侧有序，min 在左侧或就是 mid
                # 注意：这里千万别减 1，因为 mid 可能是最小值
                right = mid
            else:
                # nums[mid] == nums[right]
                # 【核心修复】：在删掉 right 之前，看一眼它是不是那个"断崖点"
                # 如果当前值比前一个值小，说明 right 就是我们要找的 Pivot
                if right > 0 and nums[right] < nums[right - 1]:
                    return right
                
                # 如果不是断崖，才能安全移除
                right -= 1
                
        return 0



    def binarySearch(self, nums: List[int], left: int, right: int, target: int) -> bool:
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False