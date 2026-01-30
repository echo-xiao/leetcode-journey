# 278. 第一个错误的版本

**难度**: Easy | **标签**: `Binary Search` `Interactive`

## 题目描述

<p>你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。</p>

<p>假设你有 <code>n</code> 个版本 <code>[1, 2, ..., n]</code>，你想找出导致之后所有版本出错的第一个错误的版本。</p>

<p>你可以通过调用&nbsp;<code>bool isBadVersion(version)</code>&nbsp;接口来判断版本号 <code>version</code> 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。</p>
&nbsp;

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 5, bad = 4
<strong>输出：</strong>4
<strong>解释：</strong>
<code>调用 isBadVersion(3) -&gt; false 
调用 isBadVersion(5)&nbsp;-&gt; true 
调用 isBadVersion(4)&nbsp;-&gt; true</code>
<code>所以，4 是第一个错误的版本。</code>
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1, bad = 1
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= bad &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是使用二分查找法在版本序列中找到第一个错误的版本。

2. 综合思路：
   - 递归解法：通过递归调用辅助函数 `helper`，在每次调用中更新搜索区间的左右边界，直到找到第一个错误的版本。
   - 迭代解法：使用循环迭代的方式，在每次迭代中更新搜索区间的左右边界，直到找到第一个错误的版本。

3. 全量伪代码：
   - 递归解法：
     ```
     定义函数 firstBadVersion(n)
         返回 helper(n, 1, n)
     
     定义辅助函数 helper(n, left, right)
         计算 mid 为 left 和 right 的中间值
         
         如果 left 大于 right
             返回 left
         
         如果 mid 版本不是错误版本
             返回 helper(n, mid + 1, right)
         否则
             返回 helper(n, left, mid - 1)
     ```
   
   - 迭代解法：
     ```
     定义函数 firstBadVersion(n)
         初始化 left 为 1, right 为 n
         
         当 left 小于等于 right 时
             计算 mid 为 left 和 right 的中间值
             
             如果 mid 版本不是错误版本
                 更新 left 为 mid + 1
             否则
                 更新 right 为 mid - 1
         
         返回 left
     ```

4. 复杂度：
   - 时间复杂度：$O(\log n)$，因为每次检查都将搜索空间减半。
   - 空间复杂度：
     - 递归解法：$O(\log n)$，由于递归调用栈的深度。
     - 迭代解法：$O(1)$，因为只使用了常数级别的额外空间。