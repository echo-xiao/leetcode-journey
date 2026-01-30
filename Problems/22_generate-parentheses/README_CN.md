# 22. 括号生成

**难度**: Medium | **标签**: `String` `Dynamic Programming` `Backtracking`

## 题目描述

<p>数字 <code>n</code>&nbsp;代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 <strong>有效的 </strong>括号组合。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 3
<strong>输出：</strong>["((()))","(()())","(())()","()(())","()()()"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>["()"]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 8</code></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过递归回溯法构建所有可能的括号组合，确保在任何时刻右括号的数量不超过左括号。

2. **简洁的中文实现思路描述：** 
   - 使用递归回溯的方法生成所有可能的括号组合。
   - 维护两个计数器，分别记录当前使用的左括号和右括号的数量。
   - 在递归过程中，只有当左括号的数量小于 `n` 时，才可以继续添加左括号；只有当右括号的数量小于左括号时，才可以继续添加右括号。
   - 当路径长度达到 `2 * n` 时，将当前路径加入结果集。

3. **总结AC版本所有的通用解决方式/逻辑的中文伪代码：**

```plaintext
函数 generateParenthesis(n):
    初始化结果列表 res
    初始化路径列表 path
    调用 backtrack(0, 0, n, path, res)
    返回 res

函数 backtrack(left, right, n, path, res):
    如果路径长度等于 2 * n:
        将路径加入结果列表 res
        返回

    如果 left < n:
        在路径中添加左括号
        调用 backtrack(left + 1, right, n, path, res)
        移除路径中的最后一个字符

    如果 right < left:
        在路径中添加右括号
        调用 backtrack(left, right + 1, n, path, res)
        移除路径中的最后一个字符
```

4. **时间复杂度和空间复杂度：**

   - 时间复杂度：生成所有合法的括号组合的时间复杂度为 $O(\frac{4^n}{\sqrt{n}})$，这是 Catalan 数的性质。
   - 空间复杂度：由于递归调用栈的深度为 $O(n)$，因此空间复杂度为 $O(n)$。