# 17. 电话号码的字母组合

**难度**: Medium | **标签**: `Hash Table` `String` `Backtracking`

## 题目描述

<p>给定一个仅包含数字&nbsp;<code>2-9</code>&nbsp;的字符串，返回所有它能表示的字母组合。答案可以按 <strong>任意顺序</strong> 返回。</p>

<p>给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。</p>

<p><img src="https://pic.leetcode.cn/1752723054-mfIHZs-image.png" style="width: 200px;" /></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>digits = "23"
<strong>输出：</strong>["ad","ae","af","bd","be","bf","cd","ce","cf"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>digits = "2"
<strong>输出：</strong>["a","b","c"]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= digits.length &lt;= 4</code></li>
	<li><code>digits[i]</code> 是范围 <code>['2', '9']</code> 的一个数字。</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：使用深度优先搜索（DFS）或回溯法遍历所有可能的字母组合，构建结果集。

2. 综合思路：
   - **递归与回溯**：所有版本都使用递归来实现深度优先搜索（DFS），通过回溯法构建每个可能的字母组合。
   - **DFS与BFS**：所有版本均采用DFS策略，没有使用广度优先搜索（BFS）。
   - **数据结构**：使用字典（哈希表）来映射数字到字母，列表用于存储当前路径和结果。

3. 全量伪代码：
   ```plaintext
   函数 letterCombinations(输入 digits: 字符串) -> 列表:
       如果 digits 为空:
           返回空列表

       初始化 mapping 为数字到字母的映射
       初始化 res 为结果列表
       调用递归函数 dfs 或 backtrack(参数: 当前索引, 当前路径, digits, mapping, res)
       返回 res

   函数 dfs 或 backtrack(参数: 当前索引, 当前路径, digits, mapping, res):
       如果 当前索引 等于 digits 的长度:
           将当前路径加入 res
           返回

       获取当前数字对应的字母列表
       对于每个字母:
           将字母加入当前路径
           递归调用 dfs 或 backtrack(参数: 当前索引+1, 当前路径, digits, mapping, res)
           从当前路径移除最后一个字母（回溯）
   ```

4. 复杂度：
   - 时间复杂度：$O(3^n \times 4^m)$，其中 $n$ 是映射到3个字母的数字个数（如2, 3, 4, 5, 6, 8），$m$ 是映射到4个字母的数字个数（如7, 9）。
   - 空间复杂度：$O(n + m)$，主要用于递归调用栈和存储结果。