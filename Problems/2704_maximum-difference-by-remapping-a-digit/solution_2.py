class Solution:
    def minMaxDifference(self, num: int) -> int:
        numList = list(str(num))
        nums = numList[:]
        target = nums[0]

        for i in range(0, len(nums)):
            if nums[i] != '9':
                target = nums[i]
                break
            
        for i in range(0, len(nums)):
            if nums[i] == target:
                nums[i] = '9'
            
        maxNum = "".join(nums)
        
        nums = numList[:]
        for i in range(0, len(nums)):
            if nums[i] != '0':
                target = nums[i]
                break

        for i in range(0, len(nums)):
            if nums[i] == target:
                nums[i] = '0'

        minNum = "".join(nums)

        return int(maxNum) - int(minNum)

        
                
        
