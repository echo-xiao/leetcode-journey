# 496. 下一个更大元素 I

**难度**: Easy | **标签**: `Array` `Hash Table` `Stack` `Monotonic Stack`

## 题目描述

<p><code>nums1</code>&nbsp;中数字&nbsp;<code>x</code>&nbsp;的 <strong>下一个更大元素</strong> 是指&nbsp;<code>x</code>&nbsp;在&nbsp;<code>nums2</code> 中对应位置 <strong>右侧</strong> 的 <strong>第一个</strong> 比&nbsp;<code>x</code><strong>&nbsp;</strong>大的元素。</p>

<p>给你两个<strong> 没有重复元素</strong> 的数组&nbsp;<code>nums1</code> 和&nbsp;<code>nums2</code> ，下标从 <strong>0</strong> 开始计数，其中<code>nums1</code>&nbsp;是&nbsp;<code>nums2</code>&nbsp;的子集。</p>

<p>对于每个 <code>0 &lt;= i &lt; nums1.length</code> ，找出满足 <code>nums1[i] == nums2[j]</code> 的下标 <code>j</code> ，并且在 <code>nums2</code> 确定 <code>nums2[j]</code> 的 <strong>下一个更大元素</strong> 。如果不存在下一个更大元素，那么本次查询的答案是 <code>-1</code> 。</p>

<p>返回一个长度为&nbsp;<code>nums1.length</code> 的数组<em> </em><code>ans</code><em> </em>作为答案，满足<em> </em><code>ans[i]</code><em> </em>是如上所述的 <strong>下一个更大元素</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [4,1,2], nums2 = [1,3,4,2].
<strong>输出：</strong>[-1,3,-1]
<strong>解释：</strong>nums1 中每个值的下一个更大元素如下所述：
- 4 ，用加粗斜体标识，nums2 = [1,3,<strong>4</strong>,2]。不存在下一个更大元素，所以答案是 -1 。
- 1 ，用加粗斜体标识，nums2 = [<em><strong>1</strong></em>,3,4,2]。下一个更大元素是 3 。
- 2 ，用加粗斜体标识，nums2 = [1,3,4,<em><strong>2</strong></em>]。不存在下一个更大元素，所以答案是 -1 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [2,4], nums2 = [1,2,3,4].
<strong>输出：</strong>[3,-1]
<strong>解释：</strong>nums1 中每个值的下一个更大元素如下所述：
- 2 ，用加粗斜体标识，nums2 = [1,<em><strong>2</strong></em>,3,4]。下一个更大元素是 3 。
- 4 ，用加粗斜体标识，nums2 = [1,2,3,<em><strong>4</strong></em>]。不存在下一个更大元素，所以答案是 -1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length &lt;= nums2.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums1</code>和<code>nums2</code>中所有整数 <strong>互不相同</strong></li>
	<li><code>nums1</code> 中的所有整数同样出现在 <code>nums2</code> 中</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你可以设计一个时间复杂度为 <code>O(nums1.length + nums2.length)</code> 的解决方案吗？</p>


---
## 解题思路与复盘

1. 一句话直击本质：使用单调栈遍历 `nums2`，记录每个元素的下一个更大元素，然后根据 `nums1` 查询结果。

2. 综合思路：
   - **单调栈解法**：通过从后向前遍历 `nums2`，使用单调栈维护一个递减序列，记录每个元素的下一个更大元素，最后根据 `nums1` 查询结果。
   - **暴力解法**：直接在 `nums2` 中找到 `nums1` 中每个元素的位置，然后向后查找第一个更大的元素。

3. 全量伪代码：
   - **单调栈解法伪代码**：
     ```
     初始化空栈 stack 和空字典 mapp
     从后向前遍历 nums2 中的每个元素 num:
         当 stack 不为空且 stack 顶部元素小于等于 num 时，弹出 stack 顶部元素
         如果 stack 为空，将 mapp[num] 设为 -1
         否则，将 mapp[num] 设为 stack 顶部元素
         将 num 压入 stack
     初始化结果列表 res
     对于 nums1 中的每个元素 num:
         将 mapp[num] 添加到 res 中
     返回 res
     ```
   - **暴力解法伪代码**：
     ```
     初始化结果列表 res，长度为 nums1 的长度，初始值为 -1
     对于 nums1 中的每个元素 num:
         找到 num 在 nums2 中的索引 idx
         从 idx+1 开始遍历 nums2:
             如果找到一个元素大于 num:
                 将该元素赋值给 res 对应位置
                 跳出循环
     返回 res
     ```

4. 复杂度：
   - **单调栈解法**：
     - 时间复杂度：$O(n + m)$，其中 $n$ 是 `nums1` 的长度，$m$ 是 `nums2` 的长度。
     - 空间复杂度：$O(m)$，用于存储栈和映射。
   - **暴力解法**：
     - 时间复杂度：$O(n \times m)$，因为对于 `nums1` 中的每个元素都可能需要遍历 `nums2`。
     - 空间复杂度：$O(1)$，不需要额外的空间（除了结果存储）。