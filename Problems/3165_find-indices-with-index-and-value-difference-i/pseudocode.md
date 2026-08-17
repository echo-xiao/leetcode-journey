# 3165. 找出满足差值条件的下标 I · 解题思路与伪代码

1. 一句话直击本质：通过遍历数组，寻找满足给定索引差和数值差条件的两个下标。

2. 综合思路：
   - **版本 1**：使用滑动窗口的思想，通过维护当前窗口内的最小和最大值的索引，快速判断是否满足条件。
   - **版本 2**：使用双重循环暴力搜索所有可能的索引对，检查是否满足条件。

3. 全量伪代码：
   - **版本 1 伪代码**：
     ```
     初始化 min_idx 和 max_idx 为 0
     遍历数组从 indexDifference 到 n-1 的每个元素 j：
         计算 i = j - indexDifference
         如果 nums[i] 小于 nums[min_idx]，更新 min_idx 为 i
         如果 nums[i] 大于 nums[max_idx]，更新 max_idx 为 i
         如果 nums[j] 与 nums[min_idx] 的差值大于等于 valueDifference，返回 [min_idx, j]
         如果 nums[j] 与 nums[max_idx] 的差值大于等于 valueDifference，返回 [max_idx, j]
     如果没有找到满足条件的下标对，返回 [-1, -1]
     ```
   - **版本 2 伪代码**：
     ```
     初始化空列表 answer
     遍历数组的每个元素 i：
         从 i + indexDifference 开始遍历数组的每个元素 j：
             如果 i 和 j 的索引差大于等于 indexDifference 且 nums[i] 和 nums[j] 的值差大于等于 valueDifference：
                 更新 answer 为 [i, j]
     如果 answer 为空，返回 [-1, -1]
     否则，返回 answer
     ```

4. 复杂度：
   - **版本 1**：
     - 时间复杂度：$O(n)$，因为每个元素最多被访问两次。
     - 空间复杂度：$O(1)$，只使用了常数个额外变量。
   - **版本 2**：
     - 时间复杂度：$O(n^2)$，因为使用了双重循环遍历所有可能的索引对。
     - 空间复杂度：$O(1)$，只使用了常数个额外变量。
