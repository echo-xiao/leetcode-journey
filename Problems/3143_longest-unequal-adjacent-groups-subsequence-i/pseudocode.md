# 3143. 最长相邻不相等子序列 I · 解题思路与伪代码

1. **一句话直击本质**：
   - 核心逻辑是通过遍历 `groups` 数组，选择相邻不相等的元素对应的 `words` 组成最长子序列。

2. **综合思路**：
   - **迭代法**：遍历 `groups` 数组，直接比较相邻元素是否相等，不相等则将对应的 `words` 元素加入结果。
   - **递归法（带记忆化）**：使用递归和记忆化搜索，尝试在每个位置选择或不选择当前元素，记录并比较选择后的最长子序列。
   - **双起点法**：分别从 `groups` 的 0 和 1 开始构建子序列，交替选择符合条件的元素，最后比较两种起点的结果。

3. **全量伪代码**：

   - **迭代法**：
     ```
     初始化结果列表 ans，包含 words 的第一个元素
     对于 i 从 1 到 len(words) - 1:
         如果 groups[i] 不等于 groups[i-1]:
             将 words[i] 加入 ans
     返回 ans
     ```

   - **递归法（带记忆化）**：
     ```
     定义 solve(i, prev) 函数:
         如果 i 等于 N，返回空列表
         如果 (i, prev) 在 memo 中，返回 memo[(i, prev)]
         初始化 maxRes 为 solve(i + 1, prev)
         如果 groups[i] 不等于 prev:
             计算 afterChoosen 为 solve(i + 1, groups[i])
             计算 ifChoosen 为 [words[i]] + afterChoosen
             如果 ifChoosen 的长度大于 maxRes 的长度:
                 更新 maxRes 为 ifChoosen
         将 maxRes 存入 memo[(i, prev)]
         返回 maxRes
     调用 solve(0, -1) 并返回结果
     ```

   - **双起点法**：
     ```
     定义 build(words, groups, start):
         初始化 res 为空列表
         设置 expected 为 start
         对于 i 从 0 到 len(words) - 1:
             如果 groups[i] 等于 expected:
                 将 words[i] 加入 res
                 切换 expected 为 1 - expected
         返回 res
     计算 start0 为 build(words, groups, 0)
     计算 start1 为 build(words, groups, 1)
     返回 start0 或 start1 中较长的一个
     ```

4. **复杂度**：
   - **迭代法**：时间复杂度 $O(n)$，空间复杂度 $O(1)$。
   - **递归法（带记忆化）**：时间复杂度 $O(n^2)$，空间复杂度 $O(n^2)$。
   - **双起点法**：时间复杂度 $O(n)$，空间复杂度 $O(n)$。
