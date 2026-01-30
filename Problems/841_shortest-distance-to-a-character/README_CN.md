# 841. 字符的最短距离

**难度**: Easy | **标签**: `Array` `Two Pointers` `String`

## 题目描述

<p>给你一个字符串 <code>s</code> 和一个字符 <code>c</code> ，且 <code>c</code> 是 <code>s</code> 中出现过的字符。</p>

<p>返回一个整数数组 <code>answer</code> ，其中 <code>answer.length == s.length</code> 且 <code>answer[i]</code> 是 <code>s</code> 中从下标 <code>i</code> 到离它 <strong>最近</strong> 的字符 <code>c</code> 的 <strong>距离</strong> 。</p>

<p>两个下标&nbsp;<code>i</code> 和 <code>j</code> 之间的 <strong>距离</strong> 为 <code>abs(i - j)</code> ，其中 <code>abs</code> 是绝对值函数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "loveleetcode", c = "e"
<strong>输出：</strong>[3,2,1,0,1,0,0,1,2,2,1,0]
<strong>解释：</strong>字符 'e' 出现在下标 3、5、6 和 11 处（下标从 0 开始计数）。
距下标 0 最近的 'e' 出现在下标 3 ，所以距离为 abs(0 - 3) = 3 。
距下标 1 最近的 'e' 出现在下标 3 ，所以距离为 abs(1 - 3) = 2 。
对于下标 4 ，出现在下标 3 和下标 5 处的 'e' 都离它最近，但距离是一样的 abs(4 - 3) == abs(4 - 5) = 1 。
距下标 8 最近的 'e' 出现在下标 6 ，所以距离为 abs(8 - 6) = 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "aaab", c = "b"
<strong>输出：</strong>[3,2,1,0]
</pre>

<p>&nbsp;</p>
<strong>提示：</strong>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s[i]</code> 和 <code>c</code> 均为小写英文字母</li>
	<li>题目数据保证 <code>c</code> 在 <code>s</code> 中至少出现一次</li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过两次遍历字符串，分别从左到右和从右到左计算每个字符到目标字符的最短距离。

2. **综合思路：**
   - **双向遍历法：** 版本 1 使用两次遍历，第一次从左到右记录每个字符到最近的目标字符的距离，第二次从右到左更新距离以确保每个字符的距离是最短的。
   - **索引列表法：** 版本 2 先记录所有目标字符的索引，然后对每个字符计算到这些索引的最小距离。

3. **全量伪代码：**

   - **双向遍历法：**
     ```
     初始化结果数组 res，长度为字符串 s 的长度，所有元素为 0
     初始化临时变量 tmp 为负无穷
     从左到右遍历字符串 s 的每个字符
         如果当前字符等于目标字符 c
             更新 tmp 为当前索引
         计算当前字符到 tmp 的距离
         将距离存入结果数组 res
     初始化临时变量 tmp 为正无穷
     从右到左遍历字符串 s 的每个字符
         如果当前字符等于目标字符 c
             更新 tmp 为当前索引
         计算当前字符到 tmp 的距离
         更新结果数组 res 中的值为当前距离和已有值的最小值
     返回结果数组 res
     ```

   - **索引列表法：**
     ```
     初始化空列表 arr 用于存储目标字符 c 的索引
     遍历字符串 s 的每个字符
         如果当前字符等于目标字符 c
             将当前索引添加到 arr
     初始化结果数组 res，长度为字符串 s 的长度，所有元素为 0
     遍历字符串 s 的每个字符
         初始化 min_dis 为一个很大的数
         遍历 arr 中的每个索引
             计算当前字符到 arr 中索引的绝对距离
             更新 min_dis 为当前距离和 min_dis 的最小值
         将 min_dis 存入结果数组 res
     返回结果数组 res
     ```

4. **复杂度：**

   - **双向遍历法：** 时间复杂度为 $O(n)$，空间复杂度为 $O(1)$（不计结果数组）。
   - **索引列表法：** 时间复杂度为 $O(n \cdot m)$，其中 $m$ 是目标字符的数量，空间复杂度为 $O(m)$。