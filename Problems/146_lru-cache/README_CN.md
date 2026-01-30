# 146. LRU 缓存

**难度**: Medium | **标签**: `Hash Table` `Linked List` `Design` `Doubly-Linked List`

## 题目描述

<div class="title__3Vvk">请你设计并实现一个满足&nbsp; <a href="https://baike.baidu.com/item/LRU" target="_blank">LRU (最近最少使用) 缓存</a> 约束的数据结构。</div>

<div class="title__3Vvk">实现 <code>LRUCache</code> 类：</div>

<div class="original__bRMd">
<div>
<ul>
	<li><code>LRUCache(int capacity)</code> 以 <strong>正整数</strong> 作为容量&nbsp;<code>capacity</code> 初始化 LRU 缓存</li>
	<li><code>int get(int key)</code> 如果关键字 <code>key</code> 存在于缓存中，则返回关键字的值，否则返回 <code>-1</code> 。</li>
	<li><code>void put(int key, int value)</code>&nbsp;如果关键字&nbsp;<code>key</code> 已经存在，则变更其数据值&nbsp;<code>value</code> ；如果不存在，则向缓存中插入该组&nbsp;<code>key-value</code> 。如果插入操作导致关键字数量超过&nbsp;<code>capacity</code> ，则应该 <strong>逐出</strong> 最久未使用的关键字。</li>
</ul>

<p>函数 <code>get</code> 和 <code>put</code> 必须以 <code>O(1)</code> 的平均时间复杂度运行。</p>
</div>
</div>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入</strong>
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
<strong>输出</strong>
[null, null, null, 1, null, -1, null, -1, 3, 4]

<strong>解释</strong>
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= capacity &lt;= 3000</code></li>
	<li><code>0 &lt;= key &lt;= 10000</code></li>
	<li><code>0 &lt;= value &lt;= 10<sup>5</sup></code></li>
	<li>最多调用 <code>2 * 10<sup>5</sup></code> 次 <code>get</code> 和 <code>put</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：使用双向链表和哈希表结合，实现最近最少使用（LRU）缓存机制，以便在常数时间内完成插入、删除和访问操作。

2. 综合思路：
   - 双向链表 + 哈希表：通过双向链表维护缓存数据的顺序，最近使用的节点放在链表头部，最少使用的节点在链表尾部；哈希表用于快速查找节点。
   - 其他可能的实现（未在代码集中出现）：可以使用其他数据结构如OrderedDict（Python内置）来实现类似功能，但本质上仍然是维护顺序和快速查找。

3. 全量伪代码：
   - 初始化：
     ```
     初始化 LRUCache 类，设置容量
     创建一个哈希表 dic 用于存储键值对
     创建两个哨兵节点 head 和 tail，形成一个空的双向链表
     ```
   - 移除节点：
     ```
     从链表中移除指定节点 node
     ```
   - 添加节点到头部：
     ```
     将节点 node 添加到链表头部
     ```
   - 获取值：
     ```
     如果键 key 不在哈希表中，返回 -1
     否则，获取节点 node
     从链表中移除 node
     将 node 添加到链表头部
     返回 node 的值
     ```
   - 插入或更新值：
     ```
     如果键 key 在哈希表中：
         更新节点 node 的值
         从链表中移除 node
         将 node 添加到链表头部
     否则：
         创建新节点 node
         将 node 添加到链表头部
         将 node 添加到哈希表中
         如果哈希表大小超过容量：
             移除链表尾部节点 lru_node
             从哈希表中删除 lru_node 的键
     ```

4. 复杂度：
   - 时间复杂度：$O(1)$，对于 `get` 和 `put` 操作，均为常数时间复杂度。
   - 空间复杂度：$O(n)$，其中 $n$ 是缓存的容量，用于存储节点和哈希表。