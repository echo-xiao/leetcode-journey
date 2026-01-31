# 17. 电话号码的字母组合

**难度**: Medium | **标签**: `Hash Table` `String` `Backtracking`

**归类**: 8. 常用数据结构 > Hash Table

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

1. 一句话直击本质：使用回溯算法遍历每个数字对应的字母组合，逐步构建并记录所有可能的字符串。

2. 综合思路：
   - **递归与回溯**：所有版本均使用递归和回溯方法，通过递归函数逐步构建字母组合，当达到目标长度时将结果加入列表。
   - **DFS（深度优先搜索）**：通过递归实现深度优先搜索，探索每个可能的字母路径。
   - **不同数据结构**：使用列表 `path` 来构建当前路径，部分版本使用字符串拼接来优化空间使用。

3. 全量伪代码：
   ```plaintext
   定义函数 letterCombinations(digits):
       如果 digits 为空:
           返回空列表

       定义数字到字母的映射 mapping
       初始化结果列表 res

       调用递归函数 dfs 或 backtrack(初始参数)

       返回结果列表 res

   定义递归函数 dfs 或 backtrack(当前索引 index, 当前路径 path, 数字串 digits, 映射 mapping, 结果列表 res):
       如果 index 等于 digits 的长度:
           将当前路径 path 转换为字符串并添加到结果列表 res
           返回

       获取当前数字对应的字母 letters
       对于每个字母 c 在 letters 中:
           将字母 c 添加到当前路径 path
           递归调用 dfs 或 backtrack(下一个索引 index+1, 更新后的路径 path, 数字串 digits, 映射 mapping, 结果列表 res)
           从当前路径 path 中移除字母 c（回溯）
   ```

4. 复杂度：
   - **时间复杂度**：$O(3^n \times 4^m)$，其中 $n$ 是对应三个字母的数字个数（如2, 3, 4, 5, 6, 8），$m$ 是对应四个字母的数字个数（如7, 9）。
   - **空间复杂度**：$O(n + m)$，用于存储递归调用栈和路径。