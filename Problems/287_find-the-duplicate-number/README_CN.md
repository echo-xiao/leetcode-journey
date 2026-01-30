# 287. 寻找重复数

**难度**: Medium | **标签**: `Array` `Two Pointers` `Binary Search` `Bit Manipulation`

## 题目描述

<p>给定一个包含&nbsp;<code>n + 1</code> 个整数的数组&nbsp;<code>nums</code> ，其数字都在&nbsp;<code>[1, n]</code>&nbsp;范围内（包括 <code>1</code> 和 <code>n</code>），可知至少存在一个重复的整数。</p>

<p>假设 <code>nums</code> 只有 <strong>一个重复的整数</strong> ，返回&nbsp;<strong>这个重复的数</strong> 。</p>

<p>你设计的解决方案必须 <strong>不修改</strong> 数组 <code>nums</code> 且只用常量级 <code>O(1)</code> 的额外空间。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,3,4,2,2]
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,1,3,4,2]
<strong>输出：</strong>3
</pre>

<p><strong>示例 3 :</strong></p>

<pre>
<strong>输入：</strong>nums = [3,3,3,3,3]
<strong>输出：</strong>3
</pre>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>nums.length == n + 1</code></li>
	<li><code>1 &lt;= nums[i] &lt;= n</code></li>
	<li><code>nums</code> 中 <strong>只有一个整数</strong> 出现 <strong>两次或多次</strong> ，其余整数均只出现 <strong>一次</strong></li>
</ul>

<p>&nbsp;</p>

<p><b>进阶：</b></p>

<ul>
	<li>如何证明 <code>nums</code> 中至少存在一个重复的数字?</li>
	<li>你可以设计一个线性级时间复杂度 <code>O(n)</code> 的解决方案吗？</li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 该算法的核心逻辑是使用二分查找结合计数法，通过比较小于等于中间值的元素数量与中间值来缩小查找范围，最终找到重复数。

2. **综合思路：**
   - **二分查找与计数法：** 所有版本都采用了二分查找的思路，通过不断调整搜索范围来逼近重复数。具体做法是计算数组中小于等于某个中间值的元素数量，并与中间值进行比较，从而判断重复数所在的区间。
   - **排序与二分查找：** 版本 4 在进行二分查找之前对数组进行了排序，这样可以直接通过排序后的数组来判断重复数的位置。

3. **全量伪代码：**

   - **二分查找与计数法：**
     ```
     初始化 left 为 1，right 为 n-1
     初始化 ans 为 -1
     当 left 小于等于 right 时：
         计算 mid 为 left 和 right 的中间值
         调用 findCnt 函数计算 nums 中小于等于 mid 的元素数量 cnt
         如果 cnt 大于 mid：
             将 ans 更新为 mid
             将 right 更新为 mid - 1
         否则：
             将 left 更新为 mid + 1
     返回 ans

     函数 findCnt(nums, mid):
         初始化 cnt 为 0
         对于 nums 中的每个元素 num：
             如果 num 小于等于 mid：
                 将 cnt 增加 1
         返回 cnt
     ```

   - **排序与二分查找：**
     ```
     对 nums 进行排序
     初始化 left 为 1，right 为 n
     当 left 小于等于 right 时：
         计算 mid 为 left 和 right 的中间值
         调用 cntLessThanMid 函数计算 nums 中小于等于 mid 的元素数量 cnt
         如果 cnt 大于 mid：
             将 right 更新为 mid - 1
         否则：
             将 left 更新为 mid + 1
     返回 left

     函数 cntLessThanMid(nums, mid):
         初始化 cnt 为 0
         对于 nums 中的每个元素 n：
             如果 n 小于等于 mid：
                 将 cnt 增加 1
         返回 cnt
     ```

4. **复杂度：**

   - **时间复杂度：** 
     - 二分查找与计数法：每次二分查找需要 $O(\log n)$ 次迭代，每次迭代中需要 $O(n)$ 的时间来计算小于等于中间值的元素数量，因此总的时间复杂度为 $O(n \log n)$。
     - 排序与二分查找：排序需要 $O(n \log n)$ 的时间，之后的二分查找与计数法同样需要 $O(n \log n)$ 的时间，因此总的时间复杂度为 $O(n \log n)$。

   - **空间复杂度：** 
     - 所有版本的空间复杂度均为 $O(1)$，因为只使用了常数级别的额外空间。