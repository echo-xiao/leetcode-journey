class Solution:
    def minMaxDifference(self, num: int) -> int:
        numList = list(str(num)) 
        
        # --- 1. 计算 MaxNum ---
        nums = numList[:] 
        target_max = nums[0] # 定义 Max 逻辑的目标变量
        
        # 查找要替换的数字 target_max
        for i in range(0, len(nums)):
            if nums[i] != '9':
                target_max = nums[i]
                break # 找到第一个非 9 的数字后退出
                
        # 执行替换
        for i in range(0, len(nums)):
            if nums[i] == target_max: # 使用 target_max
                nums[i] = '9'
                
        maxNum = "".join(nums)
        
        
        # --- 2. 计算 MinNum ---
        nums = numList[:] # 重新创建副本
        target_min = nums[0] # 定义 Min 逻辑的目标变量
        
        # 查找要替换的数字 target_min
        for i in range(0, len(nums)):
            if nums[i] != '0':
                target_min = nums[i]
                break # 找到第一个非 0 的数字后退出
                
        # 执行替换
        for i in range(0, len(nums)):
            if nums[i] == target_min: # 使用 target_min
                nums[i] = '0'
                
        minNum = "".join(nums)
        
        return int(maxNum) - int(minNum)