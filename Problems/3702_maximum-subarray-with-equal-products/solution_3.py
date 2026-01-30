import math

class Solution(object):
    def maxLength(self, nums):

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return 1 if nums[0] == 1 else 0

        # 找到数组中的最大值，以确定筛法的范围
        max_val = 0
        for num in nums:
            max_val = max(max_val, num)

        # 1. 预计算：使用筛法找到每个数的最小质因子 (SPF)
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val**0.5) + 1):
            if spf[i] == i:  # i 是一个质数
                for j in range(i * i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        # 辅助函数：根据SPF数组快速获取一个数的所有唯一质因子
        memo = {}
        def get_prime_factors(num):
            if num in memo:
                return memo[num]
            
            factors = set()
            temp_num = num
            if temp_num <= 1:
                return factors
            while temp_num > 1:
                p = spf[temp_num]
                factors.add(p)
                while temp_num % p == 0:
                    temp_num //= p
            memo[num] = factors
            return factors

        # 2. 滑动窗口寻找最长的两两互质子数组
        prime_counts = collections.defaultdict(int)
        left = 0
        max_pairwise_coprime_len = 0
        
        for right in range(n):
            # 获取当前数字的质因子并更新计数
            factors_right = get_prime_factors(nums[right])
            for p in factors_right:
                prime_counts[p] += 1
            
            # 如果窗口内有共享的质因子（计数 > 1），则从左边收缩窗口
            while True:
                has_conflict = False
                for p in factors_right:
                    if prime_counts[p] > 1:
                        has_conflict = True
                        break
                
                if not has_conflict:
                    break
                
                # 从左边移除元素
                factors_left = get_prime_factors(nums[left])
                for p in factors_left:
                    prime_counts[p] -= 1
                left += 1

            # 更新最长两两互质子数组的长度
            max_pairwise_coprime_len = max(max_pairwise_coprime_len, right - left + 1)
        
        # 3. 最终结果
        # 因为任何长度为2的子数组都满足条件，所以结果至少是2
        return max(max_pairwise_coprime_len, 2)