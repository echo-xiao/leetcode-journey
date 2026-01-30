class Solution(object):
    def sortArrayByParityII(self, nums):
        n = len(nums)
        # even_ptr 负责在偶数位上寻找“错位的奇数”
        even_ptr = 0
        # odd_ptr 负责在奇数位上寻找“错位的偶数”
        odd_ptr = 1

        while even_ptr < n and odd_ptr < n:
            # 1. even_ptr 不断前进，直到找到一个奇数
            while even_ptr < n and nums[even_ptr] % 2 == 0:
                even_ptr += 2
            
            # 2. odd_ptr 不断前进，直到找到一个偶数
            while odd_ptr < n and nums[odd_ptr] % 2 == 1:
                odd_ptr += 2
            
            # 3. 如果两个指针都还没越界，说明都找到了目标，进行交换
            if even_ptr < n and odd_ptr < n:
                nums[even_ptr], nums[odd_ptr] = nums[odd_ptr], nums[even_ptr]
            
        return nums