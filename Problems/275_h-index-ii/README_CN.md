# 275. H 指数 II

**难度**: Medium | **标签**: `Array` `Binary Search`

## 题目描述

<p>给你一个整数数组 <code>citations</code> ，其中 <code>citations[i]</code> 表示研究者的第 <code>i</code> 篇论文被引用的次数，<code>citations</code> 已经按照&nbsp;<strong>非降序排列&nbsp;</strong>。计算并返回该研究者的 h<strong><em>&nbsp;</em></strong>指数。</p>

<p><a href="https://baike.baidu.com/item/h-index/3991452?fr=aladdin" target="_blank">h 指数的定义</a>：h 代表“高引用次数”（high citations），一名科研人员的 <code>h</code> 指数是指他（她）的 （<code>n</code> 篇论文中）<strong>至少&nbsp;</strong>有 <code>h</code> 篇论文分别被引用了<strong>至少</strong> <code>h</code> 次。</p>

<p>请你设计并实现对数时间复杂度的算法解决此问题。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong><code>citations = [0,1,3,5,6]</code>
<strong>输出：</strong><code>3</code>
<strong>解释：</strong>给定数组表示研究者总共有 <code>5</code> 篇论文，每篇论文相应的被引用了 <code>0, 1, 3, 5, 6</code> 次。
&nbsp;    由于研究者有<code>3</code>篇论文每篇<strong> 至少 </strong>被引用了 <code>3</code> 次，其余两篇论文每篇被引用<strong> 不多于</strong> <code>3</code> 次，所以她的<em> h </em>指数是 <code>3</code> 。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong><code>citations = [1,2,100]</code>
<strong>输出：</strong><code>2</code>
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == citations.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= citations[i] &lt;= 1000</code></li>
	<li><code>citations</code> 按 <strong>升序排列</strong></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：利用二分查找在已排序的引用次数数组中找到满足条件的最大 H 指数。

2. 综合思路：
   - 二分查找：两种实现逻辑都采用了二分查找的思路，通过调整左右指针来逼近满足条件的最大 H 指数。
     - 版本 1：在找到 `citations[mid] == n-mid` 时直接返回结果。
     - 版本 2：通过调整左右指针，最终返回 `n-left` 作为结果。

3. 全量伪代码：
   - 初始化变量：设定 `n` 为引用次数数组的长度，`left` 为 0，`right` 为 `n-1`。
   - 二分查找循环：
     - 计算中间索引 `mid`。
     - 检查 `citations[mid]` 是否等于 `n-mid`：
       - 如果相等，返回 `n-mid`。
     - 如果 `citations[mid]` 大于 `n-mid`：
       - 版本 1：将 `right` 调整为 `mid-1`。
       - 版本 2：同样将 `right` 调整为 `mid-1`。
     - 如果 `citations[mid]` 小于 `n-mid`：
       - 将 `left` 调整为 `mid+1`。
   - 返回结果：循环结束后，返回 `n-left`。

4. 复杂度：
   - 时间复杂度：$O(\log n)$，因为使用了二分查找。
   - 空间复杂度：$O(1)$，因为只使用了常数级别的额外空间。