class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        i = 0
        while i < len(nums):
            if nums[i] >= i+1 and ((i+1==len(nums)) or (nums[i+1]<i+1)):
                return i+1
            i+=1
        return -1
            

