# 3143. 最长相邻不相等子序列 I

**难度**: Easy | **标签**: `Array` `String` `Dynamic Programming` `Greedy`

## 题目描述

<p>给定一个字符串数组&nbsp;<code>words</code>&nbsp;，和一个&nbsp;<strong>二进制</strong>&nbsp;数组&nbsp;<code>groups</code>&nbsp;，两个数组长度都是&nbsp;<code>n</code>&nbsp;。</p>

<p>如果&nbsp;<code>words</code>&nbsp;的一个 <span data-keyword="subsequence-array">子序列</span> 是交替的，那么对于序列中的任意两个连续字符串，它们在&nbsp;<code>groups</code>&nbsp;中相同索引的对应元素是 <strong>不同</strong> 的（也就是说，不能有连续的 0 或 1），</p>

<p>你需要从&nbsp;<code>words</code>&nbsp;中选出&nbsp;<strong>最长交替<span data-keyword="subsequence-array">子序列</span></strong>。</p>

<p>返回选出的子序列。如果有多个答案，返回 <strong>任意</strong> 一个。</p>

<p><b>注意：</b><code>words</code>&nbsp;中的元素是不同的&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>words = ["e","a","b"], groups = [0,0,1]
<b>输出：</b>["e","b"]
<strong>解释：</strong>一个可行的子序列是 [0,2] ，因为 groups[0] != groups[2] 。
所以一个可行的答案是 [words[0],words[2]] = ["e","b"] 。
另一个可行的子序列是 [1,2] ，因为 groups[1] != groups[2] 。
得到答案为 [words[1],words[2]] = ["a","b"] 。
这也是一个可行的答案。
符合题意的最长子序列的长度为 2 。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>words = ["a","b","c","d"], groups = [1,0,1,1]
<b>输出：</b>["a","b","c"]
<b>解释：</b>一个可行的子序列为 [0,1,2] 因为 groups[0] != groups[1] 且 groups[1] != groups[2] 。
所以一个可行的答案是 [words[0],words[1],words[2]] = ["a","b","c"] 。
另一个可行的子序列为 [0,1,3] 因为 groups[0] != groups[1] 且 groups[1] != groups[3] 。
得到答案为 [words[0],words[1],words[3]] = ["a","b","d"] 。
这也是一个可行的答案。
符合题意的最长子序列的长度为 3 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == words.length == groups.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 10</code></li>
	<li><code>groups[i]</code>&nbsp;是&nbsp;<code>0</code>&nbsp;或&nbsp;<code>1</code>。</li>
	<li><code>words</code>&nbsp;中的字符串 <strong>互不相同</strong>&nbsp;。</li>
	<li><code>words[i]</code>&nbsp;只包含小写英文字母。</li>
</ul>


---
## 解题思路与复盘

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