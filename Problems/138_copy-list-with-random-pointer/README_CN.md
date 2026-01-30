# 138. 随机链表的复制

**难度**: Medium | **标签**: `Hash Table` `Linked List`

## 题目描述

<p>给你一个长度为 <code>n</code> 的链表，每个节点包含一个额外增加的随机指针 <code>random</code> ，该指针可以指向链表中的任何节点或空节点。</p>

<p>构造这个链表的&nbsp;<strong><a href="https://baike.baidu.com/item/深拷贝/22785317?fr=aladdin" target="_blank">深拷贝</a></strong>。&nbsp;深拷贝应该正好由 <code>n</code> 个 <strong>全新</strong> 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 <code>next</code> 指针和 <code>random</code> 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。<strong>复制链表中的指针都不应指向原链表中的节点 </strong>。</p>

<p>例如，如果原链表中有 <code>X</code> 和 <code>Y</code> 两个节点，其中 <code>X.random --&gt; Y</code> 。那么在复制链表中对应的两个节点 <code>x</code> 和 <code>y</code> ，同样有 <code>x.random --&gt; y</code> 。</p>

<p>返回复制链表的头节点。</p>

<p>用一个由&nbsp;<code>n</code>&nbsp;个节点组成的链表来表示输入/输出中的链表。每个节点用一个&nbsp;<code>[val, random_index]</code>&nbsp;表示：</p>

<ul>
	<li><code>val</code>：一个表示&nbsp;<code>Node.val</code>&nbsp;的整数。</li>
	<li><code>random_index</code>：随机指针指向的节点索引（范围从&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n-1</code>）；如果不指向任何节点，则为&nbsp;&nbsp;<code>null</code>&nbsp;。</li>
</ul>

<p>你的代码 <strong>只</strong> 接受原链表的头节点 <code>head</code> 作为传入参数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/09/e1.png" style="height: 142px; width: 700px;" /></p>

<pre>
<strong>输入：</strong>head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
<strong>输出：</strong>[[7,null],[13,0],[11,4],[10,2],[1,0]]
</pre>

<p><strong class="example">示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/09/e2.png" style="height: 114px; width: 700px;" /></p>

<pre>
<strong>输入：</strong>head = [[1,1],[2,1]]
<strong>输出：</strong>[[1,1],[2,1]]
</pre>

<p><strong class="example">示例 3：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/09/e3.png" style="height: 122px; width: 700px;" /></strong></p>

<pre>
<strong>输入：</strong>head = [[3,null],[3,0],[3,null]]
<strong>输出：</strong>[[3,null],[3,0],[3,null]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 1000</code><meta charset="UTF-8" /></li>
	<li><code>-10<sup>4</sup>&nbsp;&lt;= Node.val &lt;= 10<sup>4</sup></code></li>
	<li><code>Node.random</code>&nbsp;为&nbsp;<code>null</code> 或指向链表中的节点。</li>
</ul>

<p>&nbsp;</p>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是使用哈希表存储原链表节点与新链表节点的映射关系，以便在复制链表时处理随机指针。

2. 综合思路：
   - 哈希表法：遍历链表两次，第一次创建新节点并存储映射关系，第二次设置新节点的 `next` 和 `random` 指针。
   - 其他可能解法（未在提供的代码中出现）：可以使用原地修改法，通过在原链表中插入新节点，然后分离出新链表。

3. 全量伪代码：
   - 哈希表法：
     ```
     如果头节点为空，返回空
     初始化 curr 为头节点
     初始化 oldNode 为一个空字典

     第一次遍历链表：
     对于每个节点 curr：
         创建新节点并存储在 oldNode 中，键为 curr，值为新节点
         移动 curr 到下一个节点

     第二次遍历链表：
     重置 curr 为头节点
     对于每个节点 curr：
         从 oldNode 中获取新节点 newNode
         如果 curr 有 next，设置 newNode.next 为 oldNode[curr.next]
         如果 curr 有 random，设置 newNode.random 为 oldNode[curr.random]
         移动 curr 到下一个节点

     返回 oldNode[head]
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是链表节点的数量，因为我们需要遍历链表两次。
   - 空间复杂度：$O(n)$，因为我们使用了一个哈希表来存储原节点与新节点的映射关系。