class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        n = len(nums)

        for i in range(0, n):
            left, right = i+1, n-1
            while left < right:
                ttl = nums[i] + nums[left] + nums[right]
                if abs(ttl - target) < abs(closest - target):
                    closest = ttl
                if ttl > target:
                    right -= 1
                elif ttl < target:
                    left += 1
                else:
                    return ttl
        return closest
            
            

