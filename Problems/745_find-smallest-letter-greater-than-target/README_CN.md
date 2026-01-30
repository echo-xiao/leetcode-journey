# 745. 寻找比目标字母大的最小字母

**难度**: Easy | **标签**: `Array` `Binary Search`

## 题目描述

<p>给你一个字符数组 <code>letters</code>，该数组按<strong>非递减顺序</strong>排序，以及一个字符 <code>target</code>。<code>letters</code>&nbsp;里<strong>至少有两个不同</strong>的字符。</p>

<p>返回&nbsp;<code>letters</code>&nbsp;中大于 <code>target</code> 的最小的字符。如果不存在这样的字符，则返回&nbsp;<code>letters</code> 的第一个字符。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入: </strong>letters = ['c', 'f', 'j']，target = 'a'
<strong>输出:</strong> 'c'
<strong>解释：</strong>letters 中字典上比 'a' 大的最小字符是 'c'。</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> letters = ['c','f','j'], target = 'c'
<strong>输出:</strong> 'f'
<strong>解释：</strong>letters 中字典顺序上大于 'c' 的最小字符是 'f'。</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> letters = ['x','x','y','y'], target = 'z'
<strong>输出:</strong> 'x'
<strong>解释：</strong>letters 中没有一个字符在字典上大于 'z'，所以我们返回 letters[0]。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= letters.length &lt;= 10<sup>4</sup></code></li>
	<li><code>letters[i]</code>&nbsp;是一个小写字母</li>
	<li><code>letters</code> 按<strong>非递减顺序</strong>排序</li>
	<li><code>letters</code> 最少包含两个不同的字母</li>
	<li><code>target</code> 是一个小写字母</li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 该算法的核心逻辑是利用二分查找在有序字符数组中寻找比目标字母大的最小字母。

2. **综合思路：**
   - **递归二分查找：** 通过递归的方式实现二分查找，逐步缩小查找范围，直到找到比目标字母大的最小字母。
   - **迭代二分查找：** 通过迭代的方式实现二分查找，使用循环来调整查找范围，最终找到目标字母。

3. **全量伪代码：**

   - **递归二分查找：**
     ```
     函数 nextGreatestLetter(letters, target):
         调用 helper(letters, target, 0, len(letters) - 1)
         返回 letters[index % len(letters)]

     函数 helper(letters, target, left, right):
         如果 left > right:
             返回 left
         
         mid = left + (right - left) // 2
         
         如果 letters[mid] > target:
             返回 helper(letters, target, left, mid - 1)
         否则:
             返回 helper(letters, target, mid + 1, right)
     ```

   - **迭代二分查找：**
     ```
     函数 nextGreatestLetter(letters, target):
         left = 0
         right = len(letters) - 1
         
         当 left < right:
             mid = left + (right - left) // 2
             
             如果 letters[mid] > target:
                 right = mid
             否则:
                 left = mid + 1
         
         如果 letters[left] > target:
             返回 letters[left]
         否则:
             返回 letters[0]
     ```

4. **复杂度：**
   - 时间复杂度：$O(\log n)$，因为二分查找的时间复杂度是对数级别的。
   - 空间复杂度：递归版本是 $O(\log n)$（由于递归调用栈），迭代版本是 $O(1)$。