# 456. 132 模式

**难度**: Medium | **标签**: `Array` `Binary Search` `Stack` `Monotonic Stack` `Ordered Set`

## 题目描述

<p>给你一个整数数组 <code>nums</code> ，数组中共有 <code>n</code> 个整数。<strong>132 模式的子序列</strong> 由三个整数 <code>nums[i]</code>、<code>nums[j]</code> 和 <code>nums[k]</code> 组成，并同时满足：<code>i < j < k</code> 和 <code>nums[i] < nums[k] < nums[j]</code> 。</p>

<p>如果 <code>nums</code> 中存在 <strong>132 模式的子序列</strong> ，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4]
<strong>输出：</strong>false
<strong>解释：</strong>序列中不存在 132 模式的子序列。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,1,4,2]
<strong>输出：</strong>true
<strong>解释：</strong>序列中有 1 个 132 模式的子序列： [1, 4, 2] 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [-1,3,2,0]
<strong>输出：</strong>true
<strong>解释：</strong>序列中有 3 个 132 模式的的子序列：[-1, 3, 2]、[-1, 3, 0] 和 [-1, 2, 0] 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 <= n <= 2 * 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：利用单调栈或二分查找维护一个潜在的 "32" 模式，结合前缀最小值数组来寻找 "132" 模式。

2. 综合思路：
   - **单调栈解法**：从后向前遍历数组，利用单调栈维护一个可能的 "32" 模式，确保栈顶元素是当前可用的最大 "2"，并通过更新 "k" 来寻找符合条件的 "1"。
   - **二分查找解法**：同样从后向前遍历数组，使用二分查找在一个有序列表中寻找潜在的 "2"，并结合前缀最小值数组来验证是否存在符合条件的 "1"。

3. 全量伪代码：
   - **单调栈解法伪代码**：
     ```
     初始化栈为空，k为负无穷
     从后向前遍历数组nums
         如果当前元素小于k，返回True
         当栈不为空且栈顶元素小于当前元素
             更新k为栈顶元素并弹出栈顶
         将当前元素压入栈
     返回False
     ```
   - **二分查找解法伪代码**：
     ```
     如果数组长度小于3，返回False
     初始化minArray数组，minArray[0]为nums[0]
     从1到n-1遍历数组nums
         更新minArray[i]为min(minArray[i-1], nums[i])
     初始化sortedK为空列表
     从后向前遍历数组nums
         如果nums[j]大于minArray[j]
             在sortedK中二分查找minArray[j]的插入位置idx
             如果idx小于sortedK长度且sortedK[idx]小于nums[j]，返回True
         在sortedK中二分查找nums[j]的插入位置insertPos
         将nums[j]插入sortedK的insertPos位置
     返回False
     ```
   - **二分查找辅助函数伪代码**：
     ```
     函数binarySearch(arr, target)
         初始化left为0，right为arr长度
         当left小于right
             计算mid为left和right的中间位置
             如果arr[mid]小于等于target，更新left为mid+1
             否则，更新right为mid
         返回left
     ```

4. 复杂度：
   - **单调栈解法**：时间复杂度为 $O(n)$，空间复杂度为 $O(n)$。
   - **二分查找解法**：时间复杂度为 $O(n \log n)$，空间复杂度为 $O(n)$。