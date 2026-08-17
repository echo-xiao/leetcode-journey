# 2715. K 件物品的最大和 · 解题思路与伪代码

1. 一句话直击本质：该算法的核心逻辑是优先选择尽可能多的正数1，其次选择0，最后选择负数-1，以最大化总和。

2. 综合思路：
   - 迭代解法：通过条件判断依次选择1、0和-1，确保在选择的k个物品中总和最大化。
   - 递归解法：虽然在提供的代码中没有递归实现，但可以通过递归方式逐步减少k并选择最优的物品类型。

3. 全量伪代码：
   ```
   定义函数 kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k):
       如果 k 小于等于 numOnes:
           返回 k
       否则:
           如果 k - numOnes 小于等于 numZeros:
               返回 numOnes
           否则:
               计算被迫选择的 -1 的数量 forced_neg_ones_count = k - numOnes - numZeros
               返回 numOnes - forced_neg_ones_count
   ```

4. 复杂度：
   - 时间复杂度：$O(1)$，因为算法只涉及常数次的条件判断和简单的算术运算。
   - 空间复杂度：$O(1)$，因为算法只使用了固定数量的额外变量。
