class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        left = 0
        right = 0
        max_length = 0


        while right < len(nums):
            if nums[right] - nums[left] == 1:
                max_length = max(max_length, right - left + 1)
            while nums[right] - nums[left] > 1:
                left += 1

            right += 1
                
        return max_length

        # while right < len(nums):
        #     if nums[left] == nums[right]:
        #         right += 1
        #     elif nums[left] == nums[right] - 1:
        #         cnt_length = right - left + 1
        #         max_length = max(max_length, cnt_length)
        #         right += 1
        #     else:
        #         left += 1
        # return max_length






        # seen = {}
        # max_len, sum_len1, sum_len2 = 0, 0, 0
        # for i in range(0, len(nums)):
            
        #     if nums[i] in seen:
        #         seen[nums[i]] += 1
        #     elif nums[i] not in seen:
        #         seen[nums[i]] = 1

        #     if nums[i]-1 in seen:
        #         sum_len1 = seen[nums[i]] + seen[nums[i]-1]
        #     if nums[i]+1 in seen:
        #         sum_len2 = seen[nums[i]] + seen[nums[i]+1]
            
        #     max_len = max(max(max_len, sum_len1), sum_len2)
            
        # return max_len
            