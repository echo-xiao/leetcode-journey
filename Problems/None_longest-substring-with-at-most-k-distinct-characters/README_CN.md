# None. longest-substring-with-at-most-k-distinct-characters

**难度**: Unknown | **标签**: 

**归类**: 13. 其他 > 未分类

## 题目描述

暂无描述

---
## 解题思路与复盘

1. **一句话直击本质**：使用滑动窗口维护一个包含最多 `k` 个不同字符的子串，并在遍历过程中更新最大长度。

2. **综合思路**：
   - **滑动窗口**：通过双指针（`left` 和 `right`）构建一个动态窗口，窗口内的字符种类不超过 `k`，并在移动窗口时更新最大长度。
   - **数据结构**：使用列表 `res` 来存储当前窗口内的字符，并通过集合来判断字符种类数。

3. **全量伪代码**：
   ```plaintext
   定义函数 lengthOfLongestSubstringKDistinct(s, k)
       将字符串 s 转换为字符列表 string
       初始化窗口左边界 left 为 0
       初始化窗口右边界 right 为 0
       初始化最大长度 maxLen 为 0
       初始化列表 res 用于存储当前窗口内的字符

       当 right 小于字符串长度时，执行以下步骤：
           将 string[right] 添加到 res
           将 right 增加 1

           当 res 中不同字符的数量大于 k 时，执行以下步骤：
               删除 res 中的第一个字符
               将 left 增加 1

           更新 maxLen 为 max(maxLen, right - left)

       返回 maxLen
   ```

4. **复杂度**：
   - 时间复杂度：$O(n)$，其中 $n$ 是字符串的长度。每个字符最多被访问两次（一次通过 `right` 指针，一次通过 `left` 指针）。
   - 空间复杂度：$O(k)$，用于存储当前窗口内的字符。