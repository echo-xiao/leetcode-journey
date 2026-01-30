# 89. 格雷编码

**难度**: Medium | **标签**: `Math` `Backtracking` `Bit Manipulation`

## 题目描述

<strong>n 位格雷码序列</strong> 是一个由 <code>2<sup>n</sup></code> 个整数组成的序列，其中：
<ul>
	<li>每个整数都在范围 <code>[0, 2<sup>n</sup> - 1]</code> 内（含 <code>0</code> 和 <code>2<sup>n</sup> - 1</code>）</li>
	<li>第一个整数是 <code>0</code></li>
	<li>一个整数在序列中出现 <strong>不超过一次</strong></li>
	<li>每对 <strong>相邻</strong> 整数的二进制表示 <strong>恰好一位不同</strong> ，且</li>
	<li><strong>第一个</strong> 和 <strong>最后一个</strong> 整数的二进制表示 <strong>恰好一位不同</strong></li>
</ul>

<p>给你一个整数 <code>n</code> ，返回任一有效的 <strong>n 位格雷码序列</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>[0,1,3,2]
<strong>解释：</strong>
[0,1,3,2] 的二进制表示是 [00,01,11,10] 。
- 0<strong><em>0</em></strong> 和 0<em><strong>1</strong></em> 有一位不同
- <em><strong>0</strong></em>1 和 <em><strong>1</strong></em>1 有一位不同
- 1<em><strong>1</strong></em> 和 1<em><strong>0</strong></em> 有一位不同
- <em><strong>1</strong></em>0 和 <em><strong>0</strong></em>0 有一位不同
[0,2,3,1] 也是一个有效的格雷码序列，其二进制表示是 [00,10,11,01] 。
- <em><strong>0</strong></em>0 和 <em><strong>1</strong></em>0 有一位不同
- 1<em><strong>0</strong></em> 和 1<em><strong>1</strong></em> 有一位不同
- <em><strong>1</strong></em>1 和 <em><strong>0</strong></em>1 有一位不同
- 0<em><strong>1</strong></em> 和 0<em><strong>0</strong></em> 有一位不同
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>[0,1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 16</code></li>
</ul>


---
## 解题思路与复盘

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