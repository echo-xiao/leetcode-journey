class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')

        # 1. 构建前缀和数组
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

        # 2. 遍历所有可能的子数组长度和起点
        for size in range(l, r + 1):
            for i in range(n - size + 1):
                # j 是子数组的结束点索引
                j = i + size - 1
                
                # 3. 使用前缀和 O(1) 计算子数组的和
                current_sum = prefix[j + 1] - prefix[i]
                
                if current_sum > 0:
                    min_sum = min(min_sum, current_sum)

        # 如果 min_sum 没有被更新过，说明没有找到满足条件的子数组
        if min_sum == float('inf'):
            return -1
        else:
            return min_sum