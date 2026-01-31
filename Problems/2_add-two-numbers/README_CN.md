# 2. 两数相加

**难度**: Medium | **标签**: `Linked List` `Math` `Recursion`

**归类**: 9. 数学算法 > Linked List

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

1. **一句话直击本质：**  
   使用链表节点逐位相加并处理进位，或将链表转换为整数相加后再转换回链表。

2. **综合思路：**  
   - **迭代法：**  
     通过迭代遍历两个链表，逐位相加，同时处理进位，构建结果链表。
   - **转换法：**  
     将链表转换为整数，进行整数相加后，再将结果转换回链表。

3. **全量伪代码：**

   - **迭代法：**
     ```
     初始化一个虚拟头节点 dummy 和当前节点 curr 指向 dummy
     初始化进位 carry 为 0
     当 l1 或 l2 或 carry 不为 0 时：
         如果 l1 不为空，取 l1 的值 v1，否则 v1 为 0
         如果 l2 不为空，取 l2 的值 v2，否则 v2 为 0
         计算总和 ttl = v1 + v2 + carry
         更新进位 carry = ttl // 10
         计算当前位的值 val = ttl % 10
         创建新节点，值为 val，连接到 curr 的 next
         移动 curr 到下一个节点
         如果 l1 不为空，移动 l1 到下一个节点
         如果 l2 不为空，移动 l2 到下一个节点
     返回 dummy 的 next
     ```

   - **转换法：**
     ```
     定义 transform 函数，将链表转换为整数：
         初始化空列表 res
         遍历链表，将每个节点的值添加到 res
         反转 res
         如果 res 为空，返回 0
         将 res 转换为字符串并连接，转换为整数返回

     调用 transform 函数，将 l1 和 l2 转换为整数 ans1 和 ans2
     计算总和 nums = ans1 + ans2
     将 nums 转换为字符串
     初始化一个虚拟头节点 dummy 和当前节点 curr 指向 dummy
     反向遍历字符串 nums 的每个字符：
         将字符转换为整数，创建新节点，连接到 curr 的 next
         移动 curr 到下一个节点
     返回 dummy 的 next
     ```

4. **复杂度：**

   - **迭代法：**  
     时间复杂度：$O(\max(m, n))$，其中 $m$ 和 $n$ 是两个链表的长度。  
     空间复杂度：$O(\max(m, n))$，用于存储结果链表。

   - **转换法：**  
     时间复杂度：$O(m + n)$，转换链表为整数和整数相加的时间。  
     空间复杂度：$O(m + n)$，用于存储转换后的整数和结果链表。