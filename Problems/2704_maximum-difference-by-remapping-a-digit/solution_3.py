class Solution:
    def minMaxDifference(self, num: int) -> int:
        numList = list(str(num))
        nums = numList[:]
        targetMax = nums[0]

        for i in range(0, len(nums)):
            if nums[i] != '9':
                targetMax = nums[i]
                break
            
        for i in range(0, len(nums)):
            if nums[i] == targetMax:
                nums[i] = '9'
            
        maxNum = "".join(nums)
        
        targetMin = nums[0]
        nums = numList[:]
        for i in range(0, len(nums)):
            if nums[i] != '0':
                targetMin = nums[i]
                break

        for i in range(0, len(nums)):
            if nums[i] == targetMin:
                nums[i] = '0'

        minNum = "".join(nums)

        return int(maxNum) - int(minNum)

        
                
        
