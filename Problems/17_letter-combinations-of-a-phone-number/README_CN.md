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

1. **一句话直击本质：** 通过递归回溯遍历每个数字对应的字母组合，构建所有可能的字符串。

2. **综合思路：**
   - **递归回溯（DFS）：** 所有版本都使用了递归回溯的方法，通过深度优先搜索（DFS）遍历每个数字对应的字母组合，构建所有可能的字符串。
   - **路径构建方式：** 
     - 部分版本（如版本 1 和 2）使用列表 `path` 来构建路径，通过 `append` 和 `pop` 操作来维护当前路径。
     - 其他版本（如版本 6）直接使用字符串拼接来构建路径。
   - **函数命名：** 有的版本将递归函数命名为 `dfs`，有的版本命名为 `backtrack`，但逻辑上没有本质区别。

3. **全量伪代码：**

   ```plaintext
   定义函数 letterCombinations(输入: digits)
       如果 digits 为空，返回空列表

       定义数字到字母的映射 mapping
       初始化结果列表 res

       调用递归函数 backtrack(索引 0, 空路径, digits, mapping, res)

       返回 res

   定义递归函数 backtrack(输入: 当前索引 index, 当前路径 path, digits, mapping, res)
       如果 index 等于 digits 的长度
           将当前路径加入结果列表 res
           返回

       获取当前数字对应的字母列表 letters

       对于每个字母 c 在 letters 中
           将字母 c 加入当前路径
           递归调用 backtrack(索引 index+1, 更新后的路径, digits, mapping, res)
           从当前路径中移除字母 c（如果路径是列表）
   ```

4. **复杂度：**

   - **时间复杂度：** $O(3^n \times 4^m)$，其中 $n$ 是对应于数字 2, 3, 4, 5, 6, 8 的个数，$m$ 是对应于数字 7, 9 的个数，因为这些数字对应的字母数不同。
   - **空间复杂度：** $O(n + m)$，主要用于递归调用栈和存储结果。