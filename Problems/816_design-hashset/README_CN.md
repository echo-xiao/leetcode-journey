# 816. 设计哈希集合

**难度**: Easy | **标签**: `Array` `Hash Table` `Linked List` `Design` `Hash Function`

## 题目描述

<p>不使用任何内建的哈希表库设计一个哈希集合（HashSet）。</p>

<p>实现 <code>MyHashSet</code> 类：</p>

<ul>
	<li><code>void add(key)</code> 向哈希集合中插入值 <code>key</code> 。</li>
	<li><code>bool contains(key)</code> 返回哈希集合中是否存在这个值 <code>key</code> 。</li>
	<li><code>void remove(key)</code> 将给定值 <code>key</code> 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。</li>
</ul>
&nbsp;

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
<strong>输出：</strong>
[null, null, null, true, false, null, true, null, false]

<strong>解释：</strong>
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // 返回 True
myHashSet.contains(3); // 返回 False ，（未找到）
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // 返回 True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // 返回 False ，（已移除）</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= key &lt;= 10<sup>6</sup></code></li>
	<li>最多调用 <code>10<sup>4</sup></code> 次 <code>add</code>、<code>remove</code> 和 <code>contains</code></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 使用链地址法解决哈希冲突，通过链表存储同一哈希桶中的元素。

2. **综合思路：**
   - **链地址法：** 使用固定大小的数组（哈希桶），每个桶中使用链表存储元素，解决哈希冲突。
   - **哈希函数：** 使用简单的取模运算 `key % capacity` 来确定元素存储的桶位置。
   - **链表操作：** 在链表中进行插入、删除和查找操作。

3. **全量伪代码：**

   ```plaintext
   类 MyHashSet:
       初始化方法:
           设置容量为10000
           创建一个大小为容量的数组，每个元素是一个链表节点

       方法 添加(key):
           计算索引 = key 取模 容量
           获取对应索引的链表头节点
           遍历链表:
               如果找到节点值等于key:
                   返回
           创建新节点
           将新节点插入到链表头部

       方法 删除(key):
           计算索引 = key 取模 容量
           获取对应索引的链表头节点
           初始化前一个节点为头节点
           遍历链表:
               如果找到节点值等于key:
                   将前一个节点的下一个指向当前节点的下一个
                   返回
               更新前一个节点和当前节点为下一个节点

       方法 包含(key):
           计算索引 = key 取模 容量
           获取对应索引的链表头节点
           遍历链表:
               如果找到节点值等于key:
                   返回 真
           返回 假
   ```

4. **复杂度：**

   - **时间复杂度：** 
     - 添加、删除和查找操作的平均时间复杂度为 $O(1)$，最坏情况下为 $O(n)$，其中 $n$ 是链表的长度。
   - **空间复杂度：** 
     - 空间复杂度为 $O(n + k)$，其中 $n$ 是存储的元素数量，$k$ 是哈希桶的数量（固定为10000）。