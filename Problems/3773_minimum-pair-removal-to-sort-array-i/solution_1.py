class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        while True:
            if_non_decreasing = True
            for j in range(len(nums)-1):
                if nums[j] > nums[j+1]:
                    if_non_decreasing = False
                    break

            if if_non_decreasing:
                break            

            min_sum = 1000000000
    
            for i in range(len(nums)-1):
                tmp_sum = nums[i] + nums[i+1]
                if min_sum > tmp_sum:
                    min_sum = tmp_sum
                    tmp_index = i

            del nums[tmp_index+1]
            del nums[tmp_index]
            nums.insert(tmp_index, min_sum)
            cnt += 1

        return cnt

                







            
            