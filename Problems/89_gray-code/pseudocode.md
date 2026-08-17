# 89. 格雷编码 · 解题思路与伪代码

1. 一句话直击本质：通过递归深度优先搜索（DFS）和位运算生成格雷编码序列，确保每个相邻数字之间的汉明距离为1。

2. 综合思路：
   - 递归与DFS：所有版本都使用递归的深度优先搜索（DFS）方法，通过位运算生成下一个可能的格雷编码，并使用集合记录已访问的编码以避免重复。
   - 位运算：通过异或操作（`curr ^ (1 << i)`)来生成下一个编码，确保只改变当前编码的一个位。

3. 全量伪代码：
   ```plaintext
   定义函数 grayCode(n):
       初始化结果列表 res 为 [0]
       初始化已访问集合 visited 为 {0}
       计算总数 cnt 为 2 的 n 次方
       调用递归函数 dfs(0, n, cnt, visited, res)
       返回 res

   定义递归函数 dfs(curr, n, cnt, visited, res):
       如果 res 的长度等于 cnt:
           返回 True

       对于 i 从 0 到 n-1:
           计算下一个编码 nxt 为 curr 异或 (1 左移 i 位)
           如果 nxt 不在 visited 中:
               将 nxt 加入 visited
               将 nxt 加入 res
               如果 dfs(nxt, n, cnt, visited, res) 返回 True:
                   返回 True
               从 res 中移除最后一个元素
               从 visited 中移除 nxt

       返回 False
   ```

4. 复杂度：
   - 时间复杂度：$O(2^n \cdot n)$，因为对于每个可能的编码（$2^n$个），我们最多需要检查 $n$ 个位。
   - 空间复杂度：$O(2^n)$，用于存储结果列表和已访问集合。
