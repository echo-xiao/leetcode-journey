# class Solution:
#     def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
#         n = len(nums)
#         min_sum = float('inf')

#         prefix = [0] * (n + 1)
#         for i in range(n):
#             prefix[i+1] = prefix[i] + nums[i]

#         for size in range(l, r + 1):
#             for i in range(n - size + 1):
#                 j = i + size - 1
                
#                 current_sum = prefix[j + 1] - prefix[i]
                
#                 if current_sum > 0:
#                     min_sum = min(min_sum, current_sum)

#         if min_sum == float('inf'):
#             return -1
#         else:
#             return min_sum

#         # 前缀和 & 滑动窗口



import bisect

class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')

        # 1. 构建前缀和数组
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # sorted_window 维护一个有序的、滑动窗口内的前缀和
        # 窗口对应的前缀和索引范围是 [j-r, j-l]
        sorted_window = []
        
        # 2. 循环，j 是子数组结束点 j (在 prefix 数组中是 j+1)
        for j in range(l, n + 1):
            # 3. 维护滑动窗口和有序集合
            # 当 j 第一次到达 l 时，初始化窗口
            if j == l:
                # 窗口包含 prefix[0] 到 prefix[l-l=0]
                for k in range(j - l + 1): # 此时 k=0
                    sorted_window.append(prefix[k])
            else:
                # 窗口滑动：移除旧的 prefix[j-r-1], 添加新的 prefix[j-l]
                # 注意：为了简化代码，这里没有写高效的 remove，实际应用需要更复杂的数据结构
                # 这里只演示添加逻辑，因为移除逻辑复杂且影响理解
                # 一个完整的实现需要一个能高效增删的有序数据结构
                pass

            # 为了演示，我们每次都重新构建窗口 (这会使复杂度变差，但逻辑清晰)
            # 在一个高效实现中，这一步应该是 O(logK) 的增/删操作
            window_indices = range(max(0, j - r), j - l + 1)
            sorted_window = sorted([prefix[k] for k in window_indices])

            # 4. 在有序窗口中查找
            # 寻找 < prefix[j] 的最大值
            target = prefix[j]
            # bisect_left 找到插入点，其左边的值都 < target
            idx = bisect.bisect_left(sorted_window, target)

            if idx > 0:
                # 插入点左边第一个元素就是我们要找的最佳前缀和
                best_prefix_i = sorted_window[idx - 1]
                current_sum = prefix[j] - best_prefix_i
                min_sum = min(min_sum, current_sum)

        return min_sum if min_sum != float('inf') else -1