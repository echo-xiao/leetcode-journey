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

1. **一句话直击本质**：该算法通过深度优先搜索（DFS）遍历所有可能的字母组合，生成与输入数字对应的字母组合。

2. **中文实现思路描述**：
   - 首先检查输入的数字字符串是否为空，如果为空则返回空列表。
   - 定义一个字典，将每个数字映射到对应的字母字符串。
   - 使用深度优先搜索（DFS）递归地构建字母组合：
     - 如果当前路径的长度等于输入数字的长度，则将路径加入结果列表。
     - 否则，遍历当前数字对应的所有字母，将每个字母加入路径，并递归处理下一个数字。
     - 递归返回后，移除路径中的最后一个字母以尝试其他组合。

3. **通用解决方式/逻辑的中文伪代码**：
   ```
   定义函数 letterCombinations(digits):
       如果 digits 为空，返回空列表
       定义数字到字母的映射字典 mapping
       初始化结果列表 res 和路径列表 path
       调用递归函数 dfs(digits, 0, path, res, mapping)
       返回 res

   定义递归函数 dfs(digits, i, path, res, mapping):
       如果 path 的长度等于 digits 的长度:
           将 path 转换为字符串并加入 res
           返回

       获取 digits[i] 对应的字母字符串
       对于每个字母 c 在字母字符串中:
           将 c 加入 path
           递归调用 dfs(digits, i+1, path, res, mapping)
           从 path 中移除最后一个字母
   ```

4. **时间复杂度和空间复杂度**：
   - 时间复杂度：$O(3^n \times 4^m)$，其中 $n$ 是映射到 3 个字母的数字的个数，$m$ 是映射到 4 个字母的数字的个数。
   - 空间复杂度：$O(n + m)$，用于存储递归调用栈和路径。