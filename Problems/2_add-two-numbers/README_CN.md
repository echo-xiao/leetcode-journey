# 2. 两数相加

**难度**: Medium | **标签**: `Linked List` `Math` `Recursion`

## 题目描述

<p>给你两个&nbsp;<strong>非空</strong> 的链表，表示两个非负的整数。它们每位数字都是按照&nbsp;<strong>逆序</strong>&nbsp;的方式存储的，并且每个节点只能存储&nbsp;<strong>一位</strong>&nbsp;数字。</p>

<p>请你将两个数相加，并以相同形式返回一个表示和的链表。</p>

<p>你可以假设除了数字 0 之外，这两个数都不会以 0&nbsp;开头。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/01/02/addtwonumber1.jpg" style="width: 483px; height: 342px;" />
<pre>
<strong>输入：</strong>l1 = [2,4,3], l2 = [5,6,4]
<strong>输出：</strong>[7,0,8]
<strong>解释：</strong>342 + 465 = 807.
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>l1 = [0], l2 = [0]
<strong>输出：</strong>[0]
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
<strong>输出：</strong>[8,9,9,9,0,0,0,1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>每个链表中的节点数在范围 <code>[1, 100]</code> 内</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
	<li>题目数据保证列表表示的数字不含前导零</li>
</ul>


---
## 解题思路与复盘

### 一句话直击本质

将两个链表表示的数字逐位相加，处理进位，并构造结果链表。

### 综合思路

1. **迭代法**：
   - **核心逻辑**：使用一个指针遍历两个链表，逐位相加，同时处理进位，构造结果链表。
   - **实现细节**：使用一个哑节点（dummy node）作为结果链表的起始，遍历两个链表的同时处理进位，直到所有节点和进位处理完毕。

2. **转换法**：
   - **核心逻辑**：将链表转换为整数，相加后再转换回链表。
   - **实现细节**：将链表转换为整数时，先将节点值存入列表，反转列表后拼接成字符串，再转换为整数。相加后，将结果整数转换为字符串，反转后逐位构造结果链表。

### 全量伪代码

#### 迭代法伪代码

```
初始化哑节点 dummy 和当前节点 curr 指向 dummy
初始化进位 carry 为 0

当 l1 不为空 或 l2 不为空 或 carry 不为 0 时：
    如果 l1 不为空：
        v1 = l1 的值
    否则：
        v1 = 0

    如果 l2 不为空：
        v2 = l2 的值
    否则：
        v2 = 0

    计算总和 ttl = v1 + v2 + carry
    更新进位 carry = ttl // 10
    当前位的值 val = ttl % 10

    创建新节点，值为 val，连接到 curr 的 next
    移动 curr 到 curr 的 next

    如果 l1 不为空，移动 l1 到 l1 的 next
    如果 l2 不为空，移动 l2 到 l2 的 next

返回 dummy 的 next
```

#### 转换法伪代码

```
定义 transform 函数，将链表转换为整数：
    初始化当前节点 curr 为 node
    初始化结果列表 res 为 []

    当 curr 不为空：
        将 curr 的值添加到 res
        移动 curr 到 curr 的 next

    反转 res
    如果 res 为空，返回 0

    将 res 转换为字符串并拼接成整数返回

调用 transform 函数，将 l1 和 l2 转换为整数 ans1 和 ans2
计算总和 nums = ans1 + ans2
将 nums 转换为字符串

初始化哑节点 dummy 和当前节点 curr 指向 dummy
遍历 nums 的每个字符（从后向前）：
    将字符转换为整数，创建新节点，连接到 curr 的 next
    移动 curr 到 curr 的 next

返回 dummy 的 next
```

### 复杂度

- **迭代法**：
  - 时间复杂度：$O(\max(m, n))$，其中 $m$ 和 $n$ 分别是两个链表的长度。
  - 空间复杂度：$O(\max(m, n))$，用于存储结果链表。

- **转换法**：
  - 时间复杂度：$O(m + n + k)$，其中 $m$ 和 $n$ 是链表的长度，$k$ 是结果整数的位数。
  - 空间复杂度：$O(m + n + k)$，用于存储中间列表和结果链表。