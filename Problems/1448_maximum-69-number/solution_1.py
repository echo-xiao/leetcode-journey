class Solution:
    def maximum69Number (self, num: int) -> int:
        tmp = 0
        nums = str(num)
        res = ''
        for i in range(0, len(nums)):
            if nums[i] == '9':
                res += nums[i]
            else:
                res += '9'
                res = res + nums[i+1: ]
                break
        
        return int(res)