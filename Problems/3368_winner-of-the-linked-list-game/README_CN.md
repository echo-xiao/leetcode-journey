# 3368. 链表游戏的获胜者

**难度**: Easy | **标签**: `Linked List`

## 题目描述

<p>给定一个长度为<strong>偶数</strong>的链表的<code>head</code>，链表中包含整数。</p>

<p>每个<strong>奇数索引</strong>的节点包含一个奇数，每个<strong>偶数索引</strong>的节点包含一个偶数。</p>

<p>我们将每个偶数索引的节点及其下一个节点称为<strong>一对</strong>，例如，索引为<code>0</code>和<code>1</code>的节点是一对，索引为<code>2</code>和<code>3</code>的节点是一对，依此类推。</p>

<p>对于每一<strong>对</strong>，我们比较这对节点的值：</p>

<ul>
	<li>如果奇数索引的节点值更高，则<code>&quot;Odd&quot;</code>队得一分。</li>
	<li>如果偶数索引的节点值更高，则<code>&quot;Even&quot;</code>队得一分。</li>
</ul>

<p>返回<em>得分更高的队伍的名称，如果得分相等，则返回</em> <code>&quot;Tie&quot;</code>。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1: </strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>输入: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> head = [2,1] </span></p>

<p><strong>输出: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> &quot;Even&quot; </span></p>

<p><strong>解释: </strong> 这个链表中只有一对节点，即<code>(2,1)</code>。由于<code>2 &gt; 1</code>，偶数队得分。</p>

<p>因此，答案是<code>&quot;Even&quot;</code>。</p>
</div>

<p><strong class="example">示例 2: </strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>输入: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> head = [2,5,4,7,20,5] </span></p>

<p><strong>输出: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> &quot;Odd&quot; </span></p>

<p><strong>解释: </strong> 这个链表中有<code>3</code>对节点。让我们逐一检查每一对：</p>

<p><code>(2,5)</code> -&gt; 由于<code>2 &lt; 5</code>，奇数队得分。</p>

<p><code>(4,7)</code> -&gt; 由于<code>4 &lt; 7</code>，奇数队得分。</p>

<p><code>(20,5)</code> -&gt; 由于<code>20 &gt; 5</code>，偶数队得分。</p>

<p>奇数队得了<code>2</code>分，而偶数队得了<code>1</code>分，奇数队得分更高。</p>

<p>因此，答案是<code>&quot;Odd&quot;</code>。</p>
</div>

<p><strong class="example">示例 3: </strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>输入: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> head = [4,5,2,1] </span></p>

<p><strong>输出: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> &quot;Tie&quot; </span></p>

<p><strong>解释: </strong> 这个链表中有<code>2</code>对节点。让我们逐一检查每一对：</p>

<p><code>(4,5)</code> -&gt; 由于<code>4 &lt; 5</code>，奇数队得分。</p>

<p><code>(2,1)</code> -&gt; 由于<code>2 &gt; 1</code>，偶数队得分。</p>

<p>两个队伍各得<code>1</code>分。</p>

<p>因此，答案是<code>&quot;Tie&quot;</code>。</p>
</div>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li>链表中的节点数量在<code>[2, 100]</code>范围内。</li>
	<li>链表中的节点数量为偶数。</li>
	<li><code>1 &lt;= Node.val &lt;= 100</code></li>
	<li>每个奇数索引节点的值为奇数。</li>
	<li>每个偶数索引节点的值为偶数。</li>
</ul>

---
## 解题思路与复盘

1. 一句话直击本质：算法通过遍历链表的相邻节点比较值大小，统计偶数和奇数位置的胜利次数来决定游戏的胜者。

2. 综合思路：
   - 迭代法：遍历链表，比较每对相邻节点的值，分别统计偶数和奇数位置的胜利次数，最后根据统计结果判断胜者。

3. 全量伪代码：
   ```
   定义函数 gameResult(head):
       如果 head 是空节点:
           返回 'Tie'
       
       初始化 curr 为 head
       初始化 even 和 odd 为 0

       当 curr 和 curr.next 都不是空节点时:
           如果 curr.val > curr.next.val:
               even 增加 1
           否则如果 curr.val < curr.next.val:
               odd 增加 1

           curr 移动到 curr.next.next

       如果 even > odd:
           返回 'Even'
       否则如果 even < odd:
           返回 'Odd'
       否则:
           返回 'Tie'
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是链表的节点数，因为每个节点最多被访问一次。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外变量。