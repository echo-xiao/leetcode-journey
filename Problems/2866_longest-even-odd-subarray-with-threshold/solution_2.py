class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        
        cnt = 0
        max_cnt = 0
        l = 0
        r = 0 


        while l < len(nums):
            if nums[l] % 2 == 0 and nums[l] <= threshold:
                r = l + 1
                max_cnt = max(max_cnt, 1)
                while r < len(nums):
                    if nums[r] % 2 != nums[r - 1] % 2 and nums[r] <= threshold:
                        cnt = r - l + 1
                        max_cnt = max(cnt, max_cnt)
                        r += 1
                    else:
                        break
                l = r
            else:
                l += 1
        return max_cnt
                



                

                
                
