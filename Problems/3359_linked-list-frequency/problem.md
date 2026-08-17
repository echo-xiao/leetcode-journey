# 3359. 链表频率 · 题目

**难度**: Easy | **标签**: `Hash Table` `Linked List` `Counting`

## 题目描述

<p>给定一个包含 <code>k</code> <strong>不同</strong> 元素的链表 <code>head</code>，返回一个长度为 <em>k</em> 的链表的头，该链表包含给定链表中每个 <strong>不同</strong> 元素的 <span data-keyword="frequency-linkedlist">频率</span>，顺序 <strong>可以是任意的</strong>。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1: </strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>输入: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> head = [1,1,2,1,2,3] </span></p>

<p><strong>输出: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> [3,2,1] </span></p>

<p><strong>解释: </strong> 列表中有 <code>3</code> 个不同的元素。<code>1</code> 的频率是 <code>3</code>，<code>2</code> 的频率是 <code>2</code>，<code>3</code> 的频率是 <code>1</code>。因此，我们返回 <code>3 -&gt; 2 -&gt; 1</code>。</p>

<p>注意 <code>1 -&gt; 2 -&gt; 3</code>、<code>1 -&gt; 3 -&gt; 2</code>、<code>2 -&gt; 1 -&gt; 3</code>、<code>2 -&gt; 3 -&gt; 1</code> 和 <code>3 -&gt; 1 -&gt; 2</code> 也是有效的答案。</p>
</div>

<p><strong class="example">示例 2: </strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>输入: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> head = [1,1,2,2,2] </span></p>

<p><strong>输出: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> [2,3] </span></p>

<p><strong>解释: </strong> 列表中有 <code>2</code> 个不同的元素。<code>1</code> 的频率是 <code>2</code>，<code>2</code> 的频率是 <code>3</code>。因此，我们返回 <code>2 -&gt; 3</code>。</p>
</div>

<p><strong class="example">示例 3: </strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>输入: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> head = [6,5,4,3,2,1] </span></p>

<p><strong>输出: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> [1,1,1,1,1,1] </span></p>

<p><strong>解释: </strong> 列表中有 <code>6</code> 个不同的元素。每个元素的频率都是 <code>1</code>。因此，我们返回 <code>1 -&gt; 1 -&gt; 1 -&gt; 1 -&gt; 1 -&gt; 1</code>。</p>
</div>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li>链表中的节点数量在 <code>[1, 10<sup>5</sup>]</code> 范围内。</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>
