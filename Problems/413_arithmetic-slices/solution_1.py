class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        size = len(nums)
        left, right = 0, 0
        res = []
        ttl = 0

        while right < size:
            res.append(nums[right])
            right += 1

            while len(res) >= 3 and self.calcDiff(res) is False:
                del res[0]
                left += 1

            if len(res) >= 3:
                ttl += len(res) - 2
            
        return ttl


    def calcDiff(self, nums: List[int]) -> bool:
        tag = True
        diff = nums[1] - nums[0]
        for i in range(0, len(nums)-1):
            if nums[i+1] - nums[i] != diff:
                tag = False
                break
        return tag
            
