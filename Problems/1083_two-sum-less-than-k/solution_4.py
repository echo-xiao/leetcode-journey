class Solution(object):
    def twoSumLessThanK(self, nums, k):

        nums.sort()
        n = len(nums)
        left, right = 0, n-1
        sum_num, max_num = -1, -1

        while left < right:
            sum_num = nums[left] + nums[right]
            if sum_num >= k:
                right -= 1
            elif sum_num < k:
                max_num = max(sum_num, max_num)
                left += 1                
        
        return max_num


            