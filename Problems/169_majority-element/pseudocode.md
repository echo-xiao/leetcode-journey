# 169. 多数元素 · 解题思路与伪代码

1. 一句话直击本质：
   - 版本 1：通过递归分治法将数组分成左右两部分，分别找出多数元素并比较其出现次数。
   - 版本 2 和 3：使用 Boyer-Moore 投票算法，通过计数器维护当前候选多数元素。
   - 版本 4：使用哈希表记录每个元素的出现次数，找到超过半数的元素。

2. 综合思路：
   - 分治法（版本 1）：将数组递归地分成两部分，分别找出多数元素，然后比较两部分的多数元素的出现次数，返回出现次数较多的那个。
   - Boyer-Moore 投票算法（版本 2 和 3）：遍历数组，使用计数器维护一个候选多数元素，当计数器为零时更新候选元素，最终返回候选元素。
   - 哈希表法（版本 4）：遍历数组，用哈希表记录每个元素的出现次数，当某个元素的出现次数超过半数时，返回该元素。

3. 全量伪代码：
   - 分治法：
     ```
     函数 majorityElement(nums):
         如果 nums 的长度为 1:
             返回 nums[0]
         mid = nums 的长度 // 2
         left = majorityElement(nums 的前半部分)
         right = majorityElement(nums 的后半部分)
         如果 left 出现的次数 >= right 出现的次数:
             返回 left
         否则:
             返回 right
     ```
   - Boyer-Moore 投票算法：
     ```
     函数 majorityElement(nums):
         初始化 cnt 为 0
         初始化 candidate 为 None
         对于 nums 中的每个元素 i:
             如果 cnt 为 0:
                 candidate = i
             如果 i 等于 candidate:
                 cnt 增加 1
             否则:
                 cnt 减少 1
         返回 candidate
     ```
   - 哈希表法：
     ```
     函数 majorityElement(nums):
         初始化 seen 为空字典
         对于 nums 中的每个元素 i:
             如果 i 不在 seen 中:
                 seen[i] = 1
             否则:
                 seen[i] 增加 1
             如果 seen[i] > len(nums) // 2:
                 返回 i
     ```

4. 复杂度：
   - 分治法（版本 1）：时间复杂度 $O(n \log n)$，空间复杂度 $O(\log n)$。
   - Boyer-Moore 投票算法（版本 2 和 3）：时间复杂度 $O(n)$，空间复杂度 $O(1)$。
   - 哈希表法（版本 4）：时间复杂度 $O(n)$，空间复杂度 $O(n)$。
