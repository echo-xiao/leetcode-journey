# 3359. 链表频率

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

---
## 解题思路与复盘

1. 一句话直击本质：遍历链表并使用哈希表记录每个元素的频率，然后构建一个新的链表来存储这些频率。

2. 综合思路：
   - 迭代法：通过迭代遍历链表，使用字典（哈希表）记录每个节点值出现的次数，然后再通过这些频率构建新的链表。

3. 全量伪代码：
   ```plaintext
   定义一个函数 frequenciesOfElements，输入为链表头节点 head
       初始化一个空字典 tmp 用于存储元素频率
       初始化 curr 指向 head

       当 curr 不为空时，重复以下步骤：
           如果 curr.val 不在 tmp 中：
               将 curr.val 作为键，1 作为值存入 tmp
           否则：
               将 curr.val 对应的值加 1
           将 curr 移动到下一个节点

       创建一个虚拟头节点 dummy
       初始化 curr 指向 dummy

       对于 tmp 中的每个频率值：
           创建一个新节点 new_node，其值为频率值
           将 curr.next 指向 new_node
           将 curr 移动到 curr.next

       返回 dummy.next 作为结果链表的头节点
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是链表的节点数，因为需要遍历链表两次：一次用于记录频率，一次用于构建结果链表。
   - 空间复杂度：$O(n)$，因为需要存储链表中每个不同元素的频率。