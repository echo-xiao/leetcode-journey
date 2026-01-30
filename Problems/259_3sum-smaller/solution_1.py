class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        for i in range(0, len(nums)-2):
            targetSum = target - nums[i]
            j, k = i+1, len(nums)-1

            while j < k:
                if nums[j] + nums[k] >= targetSum:
                    k -= 1
                else:
                    res += (k - j)
                    j += 1
        return res


                
